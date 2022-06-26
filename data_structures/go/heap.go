package main

type Heap interface {
	Insert(value int) []int
	Remove() ([]int, int)
}

type heap struct {
	heap []int
}

func NewHeap() Heap {
	return &heap{}
}

func (h *heap) Insert(value int) []int {
	return append(h.heap, value)
}

func (h *heap) Remove() ([]int, int) {
	return h.heap[:len(h.heap)-1], h.heap[len(h.heap)-1]
}
