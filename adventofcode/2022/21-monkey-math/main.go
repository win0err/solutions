package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const input = "data/input.txt"

const (
	RootExpr  = "root"
	HumanExpr = "humn"
)

type Expression struct {
	val     int
	op      byte
	a, b    *Expression
	isWrong bool
	parent  *Expression
}

func parseInput() (*Expression, *Expression) {
	file, err := os.Open(input)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	expresssions := make(map[string]*Expression)
	ensureExp := func(name string) *Expression {
		if _, ok := expresssions[name]; !ok {
			expresssions[name] = &Expression{}
		}

		return expresssions[name]
	}

	for scanner.Scan() {
		line := scanner.Text()

		name := string(line[:4])
		e := ensureExp(name)

		if len(line) == 17 {
			e.a = ensureExp(string(line[6:10]))
			e.a.parent = e

			e.op = line[11]

			e.b = ensureExp(string(line[13:17]))
			e.b.parent = e
		} else {
			v, _ := strconv.Atoi(line[6:])
			e.val = v
		}
	}

	for e := expresssions[HumanExpr]; e != nil; e = e.parent {
		e.isWrong = true
	}

	return expresssions[RootExpr], expresssions[HumanExpr]
}

func (e *Expression) evaluate() {
	if e.a == nil || e.b == nil {
		return
	}

	e.a.evaluate()
	e.b.evaluate()

	switch e.op {
	case '+':
		e.val = e.a.val + e.b.val
	case '-':
		e.val = e.a.val - e.b.val
	case '*':
		e.val = e.a.val * e.b.val
	case '/':
		e.val = e.a.val / e.b.val
	}
}

func (e *Expression) fixWrongArgument(newVal int) {
	e.val = newVal
	e.isWrong = false

	if e.a == nil || e.b == nil {
		return
	}

	var fixed int
	if e.a.isWrong {
		switch e.op {
		case '+':
			fixed = newVal - e.b.val
		case '-':
			fixed = newVal + e.b.val
		case '*':
			fixed = newVal / e.b.val
		case '/':
			fixed = newVal * e.b.val
		}

		e.a.fixWrongArgument(fixed)
	} else if e.b.isWrong {
		switch e.op {
		case '+':
			fixed = newVal - e.a.val
		case '-':
			fixed = e.a.val - newVal
		case '*':
			fixed = newVal / e.a.val
		case '/':
			fixed = e.a.val / newVal
		}

		e.b.fixWrongArgument(fixed)
	}

}

func main() {
	root, fixable := parseInput()
	root.evaluate()

	if root.a.isWrong {
		root.a.fixWrongArgument(root.b.val)
	} else if root.b.isWrong {
		root.a.fixWrongArgument(root.a.val)
	}

	fmt.Printf("Task 1: %d\n", root.val)
	fmt.Printf("Task 2: %d\n", fixable.val)
}
