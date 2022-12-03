package main

import (
	"bufio"
	"fmt"
	"os"
)

const input = "data/input.txt"

func parseInput() []string {
	contents := make([]string, 0)

	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		contents = append(contents, scanner.Text())
	}

	return contents
}

func getPriority(ch rune) int {
	if ch >= 'a' && ch <= 'z' {
		return int(ch) - 96
	} else if ch >= 'A' && ch <= 'Z' {
		return int(ch) - 38
	} else {
		panic("cannon calculate priority for " + string(ch))
	}
}

func intersection(head string, tail ...string) []rune {
	createSet := func(str string) map[rune]struct{} {
		s := make(map[rune]struct{}, len(str))

		for _, chr := range str {
			s[chr] = struct{}{}
		}

		return s
	}

	finalSet := createSet(head)

	for _, str := range tail {
		set := createSet(str)

		for chr := range finalSet {
			if _, has := set[chr]; !has {
				delete(finalSet, chr)
			}
		}
	}

	res := make([]rune, 0)
	for chr := range finalSet {
		res = append(res, chr)
	}

	return res
}

func main() {
	rucksacks := parseInput()
	var chr rune

	priorities := 0
	for _, backpack := range rucksacks {
		mid := len(backpack) / 2
		chr = intersection(backpack[:mid], backpack[mid:])[0]
		priorities += getPriority(chr)
	}

	groupedPriorities := 0
	for i := 0; i < len(rucksacks); i += 3 {
		chr = intersection(rucksacks[i], rucksacks[i+1], rucksacks[i+2])[0]
		groupedPriorities += getPriority(chr)
	}

	fmt.Printf("Task 1: %d\n", priorities)
	fmt.Printf("Task 2: %d\n", groupedPriorities)
}
