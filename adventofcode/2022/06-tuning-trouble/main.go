package main

import (
	"fmt"
	"os"
)

const input = "data/input.txt"

func parseInput() []byte {
	contents, err := os.ReadFile(input)
	if err != nil {
		panic(err)
	}

	return contents
}

func countBytesBeforeMarker(data []byte, seqLen int) (idx int) {
	counter := make(map[byte]int)

	for idx = 0; idx < seqLen; idx++ {
		counter[data[idx]] += 1
	}

	var removingIdx int
	for ; len(counter) < seqLen; idx++ {
		removingIdx = idx - seqLen
		counter[data[removingIdx]] -= 1

		if counter[data[removingIdx]] <= 0 {
			delete(counter, data[removingIdx])
		}

		counter[data[idx]] += 1
	}

	return
}

func main() {
	data := parseInput()

	fmt.Printf("Task 1: %d\n", countBytesBeforeMarker(data, 4))
	fmt.Printf("Task 2: %d\n", countBytesBeforeMarker(data, 14))
}
