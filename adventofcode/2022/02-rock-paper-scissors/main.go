package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const input = "data/input.txt"

func parseInput() [][]string {
	parsed := make([][]string, 0)

	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var choices []string
	for scanner.Scan() {
		choices = strings.Split(scanner.Text(), " ")
		parsed = append(parsed, choices)
	}

	return parsed
}

type Shape int

const (
	Rock     Shape = 1
	Paper    Shape = 2
	Scissors       = 3
)

func ShapeFromString(s string) Shape {
	switch s {
	case "A", "X":
		return Rock
	case "B", "Y":
		return Paper
	case "C", "Z":
		return Scissors
	default:
		panic("cannot parse shape: " + s)
	}
}

func (sh Shape) beatenBy() Shape {
	switch sh {
	case Rock:
		return Paper
	case Paper:
		return Scissors
	case Scissors:
		return Rock
	default:
		panic("unknown shape")
	}
}

func (sh Shape) beats() Shape {
	switch sh {
	case Rock:
		return Scissors
	case Paper:
		return Rock
	case Scissors:
		return Paper
	default:
		panic("unknown shape")
	}
}

func (sh Shape) GetResultAgainst(opp Shape) Result {
	if sh == opp.beatenBy() {
		return Win
	} else if sh == opp.beats() {
		return Lose
	} else {
		return Draw
	}
}

type Result int

const (
	Lose Result = 0
	Draw Result = 3
	Win         = 6
)

func ResultFromString(s string) Result {
	switch s {
	case "X":
		return Lose
	case "Y":
		return Draw
	case "Z":
		return Win
	}
	panic("cannot parse result: " + s)
}

func (res Result) MakeChoiceAgainst(opp Shape) Shape {
	if res == Win {
		return opp.beatenBy()
	} else if res == Lose {
		return opp.beats()
	}

	return opp
}

func main() {
	parsed := parseInput()

	var opp, you Shape

	task1Score := 0
	for _, round := range parsed {
		opp = ShapeFromString(round[0])
		you = ShapeFromString(round[1])

		task1Score += int(you.GetResultAgainst(opp)) + int(you)
	}

	task2Score := 0
	var expected Result
	for _, round := range parsed {
		opp = ShapeFromString(round[0])
		expected = ResultFromString(round[1])

		you = expected.MakeChoiceAgainst(opp)
		task2Score += int(expected) + int(you)
	}

	fmt.Printf("Task 1: %d\n", task1Score)
	fmt.Printf("Task 2: %d\n", task2Score)
}
