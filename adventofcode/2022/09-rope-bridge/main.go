package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const input = "data/input.txt"

type Direction byte

const (
	Up    Direction = 'U'
	Right Direction = 'R'
	Down  Direction = 'D'
	Left  Direction = 'L'
)

type Move struct {
	direction Direction
	steps     int
}

func parseInput() []Move {
	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	moves := make([]Move, 0)
	for scanner.Scan() {
		line := scanner.Text()
		count, _ := strconv.Atoi(line[2:])

		moves = append(moves, Move{direction: Direction(line[0]), steps: count})
	}

	return moves
}

type Point struct {
	x, y int
}

type Rope struct {
	knots []Point
	size  int
}

func NewRope(size int) *Rope {
	r := new(Rope)

	r.size = size
	r.knots = make([]Point, size)

	return r
}

func (r *Rope) Move(d Direction) {
	// move head
	switch d {
	case Up:
		r.knots[0].y += 1
	case Right:
		r.knots[0].x += 1
	case Down:
		r.knots[0].y -= 1
	case Left:
		r.knots[0].x -= 1
	}

	// move tail
	for i := 1; i < r.size; i++ {
		// deltas
		dx := r.knots[i-1].x - r.knots[i].x
		dy := r.knots[i-1].y - r.knots[i].y

		needsMoveX := dx == 2 || dx == -2
		needsMoveY := dy == 2 || dy == -2

		if needsMoveX && needsMoveY {
			r.knots[i].x += dx / 2 // move just one step in the same
			r.knots[i].y += dy / 2 // direction as delta, e.g. +1 or -1
		} else if needsMoveX {
			r.knots[i].x += dx / 2
			r.knots[i].y = r.knots[i-1].y
		} else if needsMoveY {
			r.knots[i].x = r.knots[i-1].x
			r.knots[i].y += dy / 2
		}
	}
}

func calcTailVisits(rope *Rope, moves []Move) int {
	visited := make(map[Point]struct{})
	for _, move := range moves {
		for i := 0; i < move.steps; i++ {
			rope.Move(move.direction)

			lastKnot := rope.knots[rope.size-1]
			visited[lastKnot] = struct{}{}
		}
	}

	return len(visited)
}

func main() {
	moves := parseInput()

	fmt.Printf("Task 1: %d\n", calcTailVisits(NewRope(2), moves))
	fmt.Printf("Task 2: %d\n", calcTailVisits(NewRope(10), moves))
}
