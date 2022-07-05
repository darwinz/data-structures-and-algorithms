from unittest import TestCase

from data_structures.python.stack import Stack

class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push("a")
        self.assertEqual("a", self.stack.peek())

    def test_pop(self):
        self.stack.push("b")
        self.stack.push("c")
        popped = self.stack.pop()
        self.assertEqual("c", popped)
        popped2 = self.stack.pop()
        self.assertEqual("b", popped2)

    def test_peek(self):
        self.stack.push("a")
        self.stack.push("z")
        self.stack.push("n")
        peeked = self.stack.peek()
        self.assertEqual("n", peeked)

    def test_size(self):
        size = 16
        for i in range(size):
            self.stack.push(i)

        current = self.stack.size()
        self.assertEqual(size, current)

        add = 5
        for i in range(add):
            self.stack.push(i)

        with_added = self.stack.size()
        self.assertEqual(size+add, with_added)
