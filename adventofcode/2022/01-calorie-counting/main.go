package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const input = "data/input.txt"

func parseInput() []int {
	calories := make([]int, 0)

	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var line string
	currentElf := 0
	for scanner.Scan() {
		line = scanner.Text()

		if line == "" {
			calories = append(calories, currentElf)
			currentElf = 0

			continue
		}

		c, _ := strconv.Atoi(line)
		currentElf += c
	}

	file.Close()

	return calories
}

func main() {
	calories := parseInput()

	// alternative: use MaxIntHeap
	sort.Slice(
		calories,
		func(i, j int) bool { return calories[i] > calories[j] },
	)

	fmt.Printf("Task 1: %d\n", calories[0])
	fmt.Printf("Task 2: %d\n", calories[0]+calories[1]+calories[2])
}
