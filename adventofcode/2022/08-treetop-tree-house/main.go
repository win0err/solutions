package main

import (
	"bufio"
	"fmt"
	"os"
)

const input = "data/input.txt"

func parseInput() Forest {
	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	forest := make([][]*Tree, 0)
	for scanner.Scan() {
		line := make([]*Tree, 0)
		for _, h := range scanner.Text() {
			line = append(line, &Tree{height: int(h - '0'), score: 1})
		}
		forest = append(forest, line)
	}

	return forest
}

type Tree struct {
	height, score int
	isVisible     bool
}

type Forest [][]*Tree

// calculate visibility and score based on previous trees in channel (side)
func calculateTreeProps(trees <-chan *Tree, forestSize int) {
	idx := 0
	lastTreeIdx := forestSize - 1

	lastIdxOfHigherThan := make(map[int]int, 10) // 0..9

	for tree := range trees {
		higherTreeIdx, hasHigherTree := lastIdxOfHigherThan[tree.height]

		if idx == 0 || idx == lastTreeIdx {
			tree.score = 0
			tree.isVisible = true
		} else {
			if !hasHigherTree {
				tree.isVisible = true
			}

			visibleDistanceUntil := 0
			if hasHigherTree {
				visibleDistanceUntil = higherTreeIdx
			}

			tree.score *= idx - visibleDistanceUntil
		}

		for h := tree.height; h >= 0; h-- {
			lastIdxOfHigherThan[h] = idx
		}

		idx++
	}
}

func (f *Forest) UpdateVisibilityAndScore() {
	forestSize := len(*f)

	var ch chan *Tree
	for line := 0; line < forestSize; line++ {
		// →
		ch = make(chan *Tree)
		go calculateTreeProps(ch, forestSize)

		for col := 0; col < forestSize; col++ {
			ch <- (*f)[line][col]
		}

		close(ch)

		// ←
		ch = make(chan *Tree)
		go calculateTreeProps(ch, forestSize)

		for col := forestSize - 1; col >= 0; col-- {
			ch <- (*f)[line][col]
		}

		close(ch)
	}

	for col := 0; col < forestSize; col++ {
		// ↓
		ch = make(chan *Tree)
		go calculateTreeProps(ch, forestSize)

		for line := 0; line < forestSize; line++ {
			ch <- (*f)[line][col]
		}

		close(ch)

		// ↑
		ch = make(chan *Tree)
		go calculateTreeProps(ch, forestSize)

		for line := forestSize - 1; line >= 0; line-- {
			ch <- (*f)[line][col]
		}

		close(ch)
	}
}

func main() {
	forest := parseInput()
	forest.UpdateVisibilityAndScore()

	visibleCount := 0
	maxScore := 0
	for _, line := range forest {
		for _, tree := range line {
			if tree.isVisible {
				visibleCount++
			}
			if tree.score > maxScore {
				maxScore = tree.score
			}
		}
	}

	fmt.Printf("Task 1: %d\n", visibleCount)
	fmt.Printf("Task 2: %d\n", maxScore)
}
