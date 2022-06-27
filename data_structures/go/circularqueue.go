package main

import "fmt"

type circularqueue struct {
	size  int
	front int
	rear  int
	queue []int
}

var size int = 5

func NewCircularQueue() Queue {
	return &circularqueue{
		size:  size,
		front: -1,
		rear:  -1,
		queue: make([]int, size),
	}
}

func (q *circularqueue) isFull() bool {
	if q.front == 0 && q.rear == q.size-1 {
		return true
	}
	if q.front == q.rear+1 {
		return true
	}
	return false
}

func (q *circularqueue) isEmpty() bool {
	return q.front == -1
}

func (q *circularqueue) Enqueue(value int) []int {
	if q.isFull() {
		fmt.Println("Queue is full")
		return q.queue
	}
	q.rear++
	q.queue[q.rear] = value
	if q.front == -1 {
		q.front = 0
	}
	return q.queue
}

func (q *circularqueue) Dequeue() ([]int, int) {
	if q.isEmpty() {
		fmt.Println("Queue is empty")
		return q.queue, 0
	}
	q.front++
	if q.front == q.size {
		q.front = 0
	}
	return q.queue, q.queue[q.front]
}

func (q *circularqueue) Peek() int {
	if q.isEmpty() {
		return 0
	}
	return q.queue[q.front]
}

func (q *circularqueue) Print() {
	for i := q.front; i <= q.rear; i++ {
		print(q.queue[i])
		print(" ")
	}
	println()
}
