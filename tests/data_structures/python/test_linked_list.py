from unittest import TestCase

from data_structures.python.linked_list import LinkedList


class TestLinkedList(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_append(self):
        self.linked_list.append("a")
        self.assertEqual("a", self.linked_list.head.data)

    def test_prepend(self):
        self.linked_list.append("a")
        self.linked_list.prepend("z")
        self.assertEqual("z", self.linked_list.head.data)

    def test_add_after(self):
        self.linked_list.append("a")
        self.linked_list.append("c")
        self.linked_list.add_after("a", "b")
        self.assertEqual("b", self.linked_list.head.next.data)

    def test_add_before(self):
        self.linked_list.append("a")
        self.linked_list.append("c")
        self.linked_list.add_before("c", "b")
        self.assertEqual("b", self.linked_list.head.next.data)

    def test_delete_with_value(self):
        self.linked_list.append("a")
        self.linked_list.append("c")
        self.linked_list.delete_with_value("c")
        self.assertIsNone(self.linked_list.head.next)
