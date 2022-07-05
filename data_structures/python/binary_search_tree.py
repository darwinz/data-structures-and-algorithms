class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, node, value):
        if value <= node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(node.right, value)

    def contains(self, node, value):
        if value == node.data:
            return True
        elif value < node.data:
            if node.left is None:
                return False
            else:
                return self.contains(node.left, value)
        else:
            if node.right is None:
                return False
            else:
                return self.contains(node.right, value)

    def in_order(self, node, output="|"):
        if node.left is not None:
            output = self.in_order(node.left, output)
        output = f"{output}{node.data}|"
        if node.right is not None:
            output = self.in_order(node.right, output)
        return output

    def pre_order(self, node, output="|"):
        output = f"{output}{node.data}|"
        if node.left is not None:
            output = self.pre_order(node.left, output)
        if node.right is not None:
            output = self.pre_order(node.right, output)
        return output

    def post_order(self, node, output="|"):
        if node.left is not None:
            output = self.post_order(node.left, output)
        if node.right is not None:
            output = self.post_order(node.right, output)
        output = f"{output}{node.data}|"
        return output
