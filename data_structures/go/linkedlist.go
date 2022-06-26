package main

import "fmt"

type Node struct {
	Value int
	Next  *Node
	Prev  *Node
}

func NewNode(value int) *Node {
	return &Node{
		Value: value,
	}
}

func (n *Node) SetNext(next *Node) {
	n.Next = next
}

func (n *Node) SetPrev(prev *Node) {
	n.Prev = prev
}

func (n *Node) GetNext() *Node {
	return n.Next
}

func (n *Node) GetPrev() *Node {
	return n.Prev
}

func (n *Node) GetValue() int {
	return n.Value
}

func (n *Node) String() string {
	return fmt.Sprintf("%d", n.Value)
}

func (n *Node) Equals(other *Node) bool {
	return n.Value == other.Value
}

func (n *Node) IsNil() bool {
	return n == nil
}

func (n *Node) IsHead() bool {
	return n.Prev == nil
}

func (n *Node) IsTail() bool {
	return n.Next == nil
}

type LinkedList struct {
	Head   *Node
	Tail   *Node
	Length int
}

func NewLinkedList() *LinkedList {
	return &LinkedList{}
}

func (l *LinkedList) IsEmpty() bool {
	return l.Length == 0
}

func (l *LinkedList) Insert(value int) {
	node := NewNode(value)
	if l.IsEmpty() {
		l.Head = node
		l.Tail = node
	} else {
		l.Tail.SetNext(node)
		node.SetPrev(l.Tail)
		l.Tail = node
	}
	l.Length++
}

func (l *LinkedList) Remove() int {
	if l.IsEmpty() {
		return 0
	}
	value := l.Head.Value
	l.Head = l.Head.GetNext()
	l.Length--
	return value
}

func (l *LinkedList) String() string {
	if l.IsEmpty() {
		return "[]"
	}
	s := "["
	node := l.Head
	for node != nil {
		s += fmt.Sprintf("%d", node.Value)
		node = node.GetNext()
		if node != nil {
			s += ", "
		}
	}
	s += "]"
	return s
}

func (l *LinkedList) AddAfter(node *Node, value int) {
	newNode := NewNode(value)
	if node.IsTail() {
		l.Tail = newNode
	} else {
		newNode.SetNext(node.GetNext())
		node.GetNext().SetPrev(newNode)
	}
	newNode.SetPrev(node)
	node.SetNext(newNode)
	l.Length++
}

func (l *LinkedList) AddBefore(node *Node, value int) {
	newNode := NewNode(value)
	if node.IsHead() {
		l.Head = newNode
	} else {
		newNode.SetPrev(node.GetPrev())
		node.GetPrev().SetNext(newNode)
	}
	newNode.SetNext(node)
	node.SetPrev(newNode)
	l.Length++
}

func (l *LinkedList) RemoveNode(node *Node) {
	if node.IsHead() {
		l.Head = node.GetNext()
	} else {
		node.GetPrev().SetNext(node.GetNext())
	}
	if node.IsTail() {
		l.Tail = node.GetPrev()
	} else {
		node.GetNext().SetPrev(node.GetPrev())
	}
	l.Length--
}
