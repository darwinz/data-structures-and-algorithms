package main

type Queue interface {
	Enqueue(value int) []int
	Dequeue() ([]int, int)
}

type queue struct {
	queue []int
}

func NewQueue() Queue {
	return &queue{}
}

func (q *queue) Enqueue(value int) []int {
	return append(q.queue, value)
}

func (q *queue) Dequeue() ([]int, int) {
	return q.queue[:len(q.queue)-1], q.queue[len(q.queue)-1]
}
