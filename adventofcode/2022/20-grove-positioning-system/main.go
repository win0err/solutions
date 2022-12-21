package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const input = "data/input.txt"

const decryptionKey = 811589153

type Node struct {
	value      int
	next, prev *Node
}

type CircularList struct {
	head  *Node
	count int
}

func parseInput(multiplier int) *CircularList {
	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	list := &CircularList{nil, 0}
	prevNode := list.head
	for scanner.Scan() {
		line := scanner.Text()
		n, _ := strconv.Atoi(line)

		node := &Node{
			value: n * multiplier,
			prev:  prevNode,
		}
		list.count++

		if prevNode != nil {
			prevNode.next = node
		} else {
			list.head = node
		}

		prevNode = node
	}

	prevNode.next = list.head
	list.head.prev = prevNode

	return list
}

func (l *CircularList) move(node *Node) {
	lastIdx := l.count - 1

	n := node.value % lastIdx
	if n < 0 {
		n += lastIdx
	}

	if n > 0 {
		after := l.getNthAfter(node, n)

		node.prev.next = node.next
		node.next.prev = node.prev

		node.prev = after
		node.next = after.next

		after.next.prev = node
		after.next = node
	}
}

func (l *CircularList) getNthAfter(node *Node, n int) *Node {
	ret := node

	n = n % l.count
	for i := 0; i < n; i++ {
		ret = ret.next
	}

	return ret
}

func (l *CircularList) mix(times int) {
	// trick is to preserve the original ordering for all mixes
	queue := make([]*Node, 0, l.count)
	for current := l.head; len(queue) != l.count; current = current.next {
		queue = append(queue, current)
	}

	for i := 0; i < times; i++ {
		for _, node := range queue {
			l.move(node)
		}
	}
}

func (l *CircularList) calcScore() int {
	var zeroNode *Node
	for zeroNode = l.head; zeroNode.value != 0; zeroNode = zeroNode.next {
		// o_0 O_O 0_o -- these guys are searching for a node with value = 0
	}

	v1000 := l.getNthAfter(zeroNode, 1000)
	v2000 := l.getNthAfter(zeroNode, 2000)
	v3000 := l.getNthAfter(zeroNode, 3000)

	return v1000.value + v2000.value + v3000.value
}

func main() {
	task1 := parseInput(1)
	task1.mix(1)

	task2 := parseInput(decryptionKey)
	task2.mix(10)

	fmt.Printf("Task 1: %d\n", task1.calcScore())
	fmt.Printf("Task 2: %d\n", task2.calcScore())
}
