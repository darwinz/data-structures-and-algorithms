from unittest import TestCase

from data_structures.python.trie import Trie


class TestTrie(TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_add_adds_trie_nodes_for_a_word(self):
        self.trie.add("dad")
        self.assertIn("d", self.trie.root.children)
        self.assertIn("a", self.trie.root.children["d"].children)
        self.assertIn("d", self.trie.root.children["d"].children["a"].children)

    def test_search(self):
        self.trie.add("dad")
        self.trie.add("jokes")
        self.assertTrue(self.trie.search("jokes"))

    def test_prefix_search(self):
        self.trie.add("daddy")
        self.trie.add("zebra")
        self.assertTrue(self.trie.prefix_search("dad"))

    def test_delete(self):
        self.trie.add("something")
        self.trie.add("else")
        self.trie.delete("else")
        self.assertNotIn("e", self.trie.root.children)
