from unittest import TestCase

from data_structures.python.tree import Node


class TestTree(TestCase):
    def setUp(self):
        self.node = Node(10)
        self.node.insert(5)
        self.node.insert(15)
        self.node.insert(8)

    def test_insert(self):
        self.assertEqual(False, self.node.contains(4))
        self.node.insert(4)
        self.assertEqual(True, self.node.contains(4))

    def test_contains(self):
        self.assertEqual(True, self.node.contains(8))

    def test_print_in_order(self):
        self.assertIn('5|8|10|15', self.node.in_order())

    def test_print_pre_order(self):
        self.assertIn('10|5|8|15', self.node.pre_order())

    def test_print_post_order(self):
        self.assertIn('8|5|15|10', self.node.post_order())
