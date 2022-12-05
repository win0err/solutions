package main

import (
	"fmt"
	"os"
	re "regexp"
	"strconv"
	"strings"
)

const input = "data/input.txt"

var moveRegex *re.Regexp = re.MustCompile(`move (\d+) from (\d+) to (\d+)`)

type Stack []byte

func (s *Stack) PopN(n int) []byte {
	old := *s

	lastIdx := len(old) - 1
	bytes, old := old[lastIdx-n+1:], old[:lastIdx-n+1]

	*s = old

	return bytes
}

func (s *Stack) Pop() byte {
	old := *s

	lastIdx := len(old) - 1
	b, old := old[lastIdx], old[:lastIdx]

	*s = old

	return b
}

func (s *Stack) Peek() byte {
	return (*s)[len(*s)-1]
}

func (s *Stack) Push(bytes ...byte) {
	*s = append(*s, bytes...)
}

type Move struct {
	count, from, to int
}

func parseInput() ([]Stack, []Move) {
	contents, err := os.ReadFile(input)
	if err != nil {
		panic(err)
	}

	stacksAndMoves := strings.Split(string(contents), "\n\n")

	rawStacks := strings.Split(stacksAndMoves[0], "\n")
	stacks := make([]Stack, len(rawStacks[0])/4+1)

	for i := len(rawStacks) - 2; i >= 0; i-- {
		line := rawStacks[i]
		for off, st := 1, 0; off < len(line); off, st = off+4, st+1 {
			if line[off] != ' ' {
				stacks[st].Push(line[off])
			}
		}
	}

	rawMoves := strings.Split(stacksAndMoves[1], "\n")
	moves := make([]Move, 0)

	for _, move := range rawMoves {
		found := moveRegex.FindStringSubmatch(move)

		count, _ := strconv.Atoi(found[1])
		from, _ := strconv.Atoi(found[2])
		to, _ := strconv.Atoi(found[3])

		moves = append(moves, Move{
			count: count,
			from:  from - 1,
			to:    to - 1,
		})
	}

	return stacks, moves
}

func main() {
	var stacks []Stack
	var moves []Move

	// CrateMover 9000
	stacks, moves = parseInput()

	for _, operation := range moves {
		for i := 0; i < operation.count; i++ {
			crate := stacks[operation.from].Pop()
			stacks[operation.to].Push(crate)
		}
	}

	result9000 := ""
	for _, stack := range stacks {
		result9000 += string(stack.Pop())
	}

	// CrateMover 9001
	stacks, moves = parseInput()

	for _, operation := range moves {
		crates := stacks[operation.from].PopN(operation.count)
		stacks[operation.to].Push(crates...)
	}

	result9001 := ""
	for _, stack := range stacks {
		result9001 += string(stack.Pop())
	}

	fmt.Printf("Task 1: %s\n", result9000)
	fmt.Printf("Task 2: %s\n", result9001)
}
