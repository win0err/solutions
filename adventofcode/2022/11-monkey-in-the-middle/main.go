package main

import (
	"fmt"
	"sort"
)

type Monkey struct {
	items           []int
	updateItem      func(old int) int
	divider         int
	ifTrue, ifFalse int
}

// parsed by hands, ha-ha
func getSample() []Monkey {
	return []Monkey{
		{
			items:      []int{79, 98},
			updateItem: func(old int) int { return old * 19 },
			divider:    23,
			ifTrue:     2,
			ifFalse:    3,
		},
		{
			items:      []int{54, 65, 75, 74},
			updateItem: func(old int) int { return old + 6 },
			divider:    19,
			ifTrue:     2,
			ifFalse:    0,
		},
		{
			items:      []int{79, 60, 97},
			updateItem: func(old int) int { return old * old },
			divider:    13,
			ifTrue:     1,
			ifFalse:    3,
		},
		{
			items:      []int{74},
			updateItem: func(old int) int { return old + 3 },
			divider:    17,
			ifTrue:     0,
			ifFalse:    1,
		},
	}
}

func getInput() []Monkey {
	return []Monkey{
		{
			items:      []int{66, 59, 64, 51},
			updateItem: func(old int) int { return old * 3 },
			divider:    2,
			ifTrue:     1,
			ifFalse:    4,
		},
		{
			items:      []int{67, 61},
			updateItem: func(old int) int { return old * 19 },
			divider:    7,
			ifTrue:     3,
			ifFalse:    5,
		},
		{
			items:      []int{86, 93, 80, 70, 71, 81, 56},
			updateItem: func(old int) int { return old + 2 },
			divider:    11,
			ifTrue:     4,
			ifFalse:    0,
		},
		{
			items:      []int{94},
			updateItem: func(old int) int { return old * old },
			divider:    19,
			ifTrue:     7,
			ifFalse:    6,
		},
		{
			items:      []int{71, 92, 64},
			updateItem: func(old int) int { return old + 8 },
			divider:    3,
			ifTrue:     5,
			ifFalse:    1,
		},
		{
			items:      []int{58, 81, 92, 75, 56},
			updateItem: func(old int) int { return old + 6 },
			divider:    5,
			ifTrue:     3,
			ifFalse:    6,
		},
		{
			items:      []int{82, 98, 77, 94, 86, 81},
			updateItem: func(old int) int { return old + 7 },
			divider:    17,
			ifTrue:     7,
			ifFalse:    2,
		},
		{
			items:      []int{54, 95, 70, 93, 88, 93, 63, 50},
			updateItem: func(old int) int { return old + 4 },
			divider:    13,
			ifTrue:     2,
			ifFalse:    0,
		},
	}
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}

	return a
}

// https://en.wikipedia.org/wiki/Least_common_multiple
func lcm(a, b int) int {
	return a * b / gcd(a, b)
}

func solve(monkeys []Monkey, rounds int, postProcess func(v int) int) int {
	items := make([][]int, len(monkeys))
	for i, monkey := range monkeys {
		items[i] = monkey.items
	}

	inspectedItemsCount := make([]int, len(monkeys))
	for round := 0; round < rounds; round++ {
		for mIdx, monkey := range monkeys {
			inspectedItemsCount[mIdx] += len(items[mIdx])

			for _, item := range items[mIdx] {
				item = monkey.updateItem(item)
				item = postProcess(item)

				dst := monkey.ifFalse
				if item%monkey.divider == 0 {
					dst = monkey.ifTrue
				}

				items[dst] = append(items[dst], item)
			}

			items[mIdx] = nil
		}
	}

	sort.Slice(inspectedItemsCount, func(i, j int) bool {
		return inspectedItemsCount[i] > inspectedItemsCount[j]
	})

	return inspectedItemsCount[0] * inspectedItemsCount[1]
}

func main() {
	monkeys := getInput()

	dividersLcm := 1
	for _, m := range monkeys {
		dividersLcm = lcm(dividersLcm, m.divider)
	}

	fmt.Printf("Task 1: %d\n", solve(monkeys, 20, func(v int) int { return v / 3 }))
	fmt.Printf("Task 2: %d\n", solve(monkeys, 10_000, func(v int) int { return v % dividersLcm }))
}
