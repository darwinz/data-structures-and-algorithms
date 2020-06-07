class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.recursive = True

    def __repr__(self):
        return f'<{Trie.list_children(self.root)}>'

    @staticmethod
    def list_children(current, output=''):
        if current.children:
            for node, child in current.children.items():
                output += node + '|'
                output = Trie.list_children(child, output)
        return output

    def add(self, word):
        if self.recursive:
            self.add_recursive(self.root, word, 0)
        else:
            self.add_iterative(word)

    def add_recursive(self, current, word, index):
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

    def add_iterative(self, word):
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

    def search(self, word):
        if self.recursive:
            return self.search_recursive(self.root, word, 0)
        else:
            return self.search_iterative(word)

    def search_iterative(self, word):
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

    def search_recursive(self, current, word, index):
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

    def prefix_search(self, prefix):
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

    def delete(self, word):
        return self.delete_recursive(self.root, word, 0)

    def delete_recursive(self, current, word, index):
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
        should_delete_current_node = self.delete(node, word, index + 1)
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
    print(trie)
    trie.search("dad")
    trie.search("doll")
    trie.search("abc")
    trie.prefix_search("oh")
    trie.prefix_search("do")
    trie.prefix_search("dad")

