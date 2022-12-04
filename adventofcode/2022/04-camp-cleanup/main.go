package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const input = "data/input.txt"

func parseInput() [][2]*Assignment {
	contents := make([][2]*Assignment, 0)

	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		rawPairs := strings.Split(scanner.Text(), ",")

		pairs := [2]*Assignment{}
		for i, rawPair := range rawPairs {
			pair := strings.Split(rawPair, "-")

			from, _ := strconv.Atoi(pair[0])
			to, _ := strconv.Atoi(pair[1])
			pairs[i] = &Assignment{from, to}
		}

		contents = append(contents, pairs)
	}

	return contents
}

type Assignment struct {
	from, to int
}

func (a *Assignment) Contains(other *Assignment) bool {
	return a.from <= other.from && a.to >= other.to
}

func (a *Assignment) Overlaps(other *Assignment) bool {
	return a.to >= other.from && a.to <= other.to || a.from >= other.from && a.from <= other.to
}

func main() {
	assignments := parseInput()

	containingCount := 0
	for _, pair := range assignments {
		if pair[0].Contains(pair[1]) || pair[1].Contains(pair[0]) {
			containingCount++
		}
	}

	overlappingCount := 0
	for _, pair := range assignments {
		if pair[0].Overlaps(pair[1]) || pair[1].Overlaps(pair[0]) {
			overlappingCount++
		}
	}

	fmt.Printf("Task 1: %d\n", containingCount)
	fmt.Printf("Task 2: %d\n", overlappingCount)
}
