package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	tree := &BinaryTree{}
	tree.insert(100).
		insert(-20).
		insert(-50).
		insert(-15).
		insert(-60).
		insert(50).
		insert(60).
		insert(55).
		insert(85).
		insert(15).
		insert(5).
		insert(-10)
	fmt.Println(os.Stdout, tree.root, 0, 'M')

	queue := NewQueue()
	queue.Enqueue(tree.root)
	queue.Enqueue(100)
	val := queue.Dequeue()
	fmt.Println(val)
	val = queue.Dequeue()
	fmt.Println(val)

	stack := NewStack()
	stack.Push(tree.root)
	stack.Push(100)
	val = stack.Pop()
	fmt.Println(val)
	val = stack.Pop()
	fmt.Println(val)

	linkedList := NewLinkedList()
	linkedList.Insert(100)
	linkedList.Insert(-20)
	linkedList.Insert(-50)
	linkedList.Insert(-15)
	fmt.Println(linkedList.String())
}

func print(w io.Writer, node *BinaryNode, ns int, ch rune) {
	if node == nil {
		return
	}

	for i := 0; i < ns; i++ {
		fmt.Fprint(w, " ")
	}
	fmt.Fprintf(w, "%c:%v\n", ch, node.data)
	fmt.Println(w, node.left, ns+2, 'L')
	fmt.Println(w, node.right, ns+2, 'R')
}
