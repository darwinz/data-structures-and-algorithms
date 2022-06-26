package main

type Stack interface {
	Push(value int) []int
	Pop() ([]int, int)
}

type stack struct {
	stack []int
}

func NewStack() Stack {
	return &stack{}
}

func (s *stack) Push(value int) []int {
	return append(s.stack, value)
}

func (s *stack) Pop() ([]int, int) {
	return s.stack[:len(s.stack)-1], s.stack[len(s.stack)-1]
}
