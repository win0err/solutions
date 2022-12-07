package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

const input = "data/input.txt"

const (
	TotalSpace    = 70_000_000
	RequiredSpace = 30_000_000
)

type Dir struct {
	children []*Dir
	parent   *Dir
	size     int
}

func parseInput() *Dir {
	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	root := new(Dir)
	currentDir := root

	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, "$ cd ") {
			dirName := line[5:]

			if dirName == ".." {
				currentDir = currentDir.parent
			} else if dirName != "/" {
				to := &Dir{parent: currentDir}
				currentDir.children = append(currentDir.children, to)
				currentDir = to
			}
		} else if line[0] >= '0' && line[0] <= '9' { // is file
			output := strings.Split(line, " ")
			size, _ := strconv.Atoi(output[0])

			for dir := currentDir; dir != nil; dir = dir.parent {
				dir.size += size
			}
		}
	}

	return root
}

func main() {
	root := parseInput()

	totalSize := 0

	usedSpace := TotalSpace - root.size
	needToFreeUp := RequiredSpace - usedSpace
	removingDirSize := math.MaxInt

	// bfs
	queue := make([]*Dir, 0)
	queue = append(queue, root)

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if len(cur.children) > 0 {
			queue = append(queue, cur.children...)
		}

		if cur.size < 100_000 {
			totalSize += cur.size
		}

		if cur.size > needToFreeUp && removingDirSize > cur.size {
			removingDirSize = cur.size
		}
	}

	fmt.Printf("Task 1: %d\n", totalSize)
	fmt.Printf("Task 2: %d\n", removingDirSize)
}
