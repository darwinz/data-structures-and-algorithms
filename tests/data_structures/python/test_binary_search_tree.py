from unittest import TestCase

from data_structures.python.binary_search_tree import Node, BinarySearchTree


class TestBinarySearchTree(TestCase):
    def setUp(self):
        self.tree = BinarySearchTree(10)

    def test_insert(self):
        self.tree.insert(self.tree.root, 5)
        self.assertEqual(5, self.tree.root.left.data)
        self.tree.insert(self.tree.root, 4)
        self.assertEqual(4, self.tree.root.left.left.data)

    def test_contains(self):
        self.tree.insert(self.tree.root, 14)
        self.assertEqual(True, self.tree.contains(self.tree.root, 14))

    def test_print_in_order(self):
        self.tree.insert(self.tree.root, 5)
        self.tree.insert(self.tree.root, 14)
        self.tree.insert(self.tree.root, 1)
        self.tree.insert(self.tree.root, 32)
        self.assertIn('1|5|10|14|32', self.tree.in_order(self.tree.root))

    def test_print_pre_order(self):
        self.tree.insert(self.tree.root, 5)
        self.tree.insert(self.tree.root, 14)
        self.tree.insert(self.tree.root, 1)
        self.tree.insert(self.tree.root, 32)
        self.assertIn('10|5|1|14|32', self.tree.pre_order(self.tree.root))

    def test_print_post_order(self):
        self.tree.insert(self.tree.root, 5)
        self.tree.insert(self.tree.root, 14)
        self.tree.insert(self.tree.root, 1)
        self.tree.insert(self.tree.root, 32)
        self.assertIn('1|5|32|14|10', self.tree.post_order(self.tree.root))
