package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const input = "data/input.txt"

func parseInput() []int {
	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	ops := make([]int, 0)
	for scanner.Scan() {
		line := scanner.Text()
		if line[:4] == "addx" {
			n, _ := strconv.Atoi(line[5:])

			// tick 1: noop (add 0)
			// tick 2: add n
			ops = append(ops, 0, n)
		} else {
			ops = append(ops, 0) // tick: noop (add 0)
		}
	}

	return ops
}

const (
	LitPixel  = '█'
	DarkPixel = ' '
	NewLine   = '\n'
)

const (
	DisplayWidth  = 40
	DisplayHeight = 6
)

func main() {
	ops := parseInput()

	spritePos := 1 // register x

	strengthsSum := 0
	imageData := make([]rune, DisplayWidth*DisplayHeight)

	const LastPixelPos = DisplayWidth - 1

	for i, instructionPayload := range ops {
		cycle := i + 1
		pixelPos := i % DisplayWidth // 0..39

		diff := pixelPos - spritePos

		var symbol rune
		if pixelPos != LastPixelPos {
			if diff >= -1 && diff <= 1 {
				symbol = LitPixel
			} else {
				symbol = DarkPixel
			}
		} else {
			symbol = NewLine
		}

		imageData = append(imageData, symbol)

		if (cycle+20)%DisplayWidth == 0 {
			strengthsSum += spritePos * cycle
		}

		spritePos += instructionPayload
	}

	fmt.Printf("Task 1: %d\n", strengthsSum)
	fmt.Printf("Task 2: \n%s\n", string(imageData))
}
