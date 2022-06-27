class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    """
    Trie is a tree-like data structure (not binary), great for
    storing and searching for words. Each node has a hash set
    (or dictionary) of possible children, each of which is a
    single letter (e.g. 'a')

    Ex.
                * (children = {'a': <TrieNode>, 'b': <TrieNode>}
              /        \
            a (ch: 'n') b
          /
        n  (end_of_word = True, children = {})
    """
    def __init__(self):
        self.root = TrieNode()
        self.recursive = True

    def __repr__(self):
        return f'<{Trie._list_children(self.root)}>'

    @staticmethod
    def _list_children(current, output='', level=1):
        if current.end_of_word:
            output += '|'
        if current.children:
            for node, child in current.children.items():
                if level == 1:
                    output += '*'
                output += node
                output = Trie._list_children(child, output, 2)
            level += 1
        return output

    def add(self, word: str) -> None:
        if self.recursive:
            self.add_recursive(self.root, word, 0)
        else:
            self.add_iterative(word)

    def add_recursive(self, current: TrieNode, word: str, index: int) -> None:
        """
        Recursive implementation of insert
        """
        if index == len(word):
            current.end_of_word = True
            return
        letter = word[index]
        node = current.children.get(letter)
        if node is None:
            node = TrieNode()
            current.children[letter] = node
        self.add_recursive(node, word, index + 1)

    def add_iterative(self, word: str) -> None:
        """
        Iterative implementation of insert
        """
        current = self.root
        for letter in word:
            node = current.children.get(letter)
            if node is None:
                node = TrieNode()
                current.children[letter] = node
            current = node
        current.end_of_word = True

    def search(self, word: str) -> bool:
        if self.recursive:
            return self.search_recursive(self.root, word, 0)
        else:
            return self.search_iterative(word)

    def search_iterative(self, word: str) -> bool:
        """
        Iterative implementation of search
        """
        current = self.root
        for letter in word:
            node = current.children.get(letter)
            if node is None:
                return False
            current = node
        return current.end_of_word

    def search_recursive(self, current: TrieNode, word: str,
                         index: int) -> bool:
        """
        Recursive implementation of search
        """
        if index == len(word):
            return current.end_of_word
        letter = word[index]
        node = current.children.get(letter)
        if node is None:
            return False
        return self.search_recursive(node, word, index + 1)

    def prefix_search(self, prefix: str) -> bool:
        """
        Search for a prefix match
        :param prefix: str - prefix part of a string
        :return: boolean
        """
        current = self.root
        for letter in prefix:
            node = current.children.get(letter)
            if node is None:
                return False
            current = node
        return True

    def delete(self, word: str) -> bool:
        return self.delete_recursive(self.root, word, 0)

    def delete_recursive(self, current: TrieNode, word: str,
                         index: int) -> bool:
        """
        Recursive implementation of delete
        """
        if index == len(word):
            if not current.end_of_word:
                return False
            current.end_of_word = False
            return len(current.children) == 0
        letter = word[index]
        node = current.children.get(letter)
        if node is None:
            return False
        should_delete_current_node = \
            self.delete_recursive(node, word, index + 1)
        if should_delete_current_node:
            del current.children[letter]
            return len(current.children) == 0
        return False


if __name__ == "__main__":
    trie = Trie()
    trie.add("dad")
    trie.add("doh")
    trie.add("daddy")
    trie.add("doll")
    trie.add("abcd")
    trie.add("acdc")
    print(trie)
    trie.search("dad")
    trie.search("doll")
    trie.search("abc")
    trie.search("zebra")
    trie.prefix_search("oh")
    trie.prefix_search("do")
    trie.prefix_search("dad")
