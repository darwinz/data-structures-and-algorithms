class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def in_order(self, output='|'):
        if self.left is not None:
            output = self.left.in_order(output)
        output = f'{output}{self.data}|'
        if self.right is not None:
            output = self.right.in_order(output)
        return output

    def pre_order(self, output='|'):
        output = f'{output}{self.data}|'
        if self.left is not None:
            output = self.left.pre_order(output)
        if self.right is not None:
            output = self.right.pre_order(output)
        return output

    def post_order(self, output='|'):
        if self.left is not None:
            output = self.left.post_order(output)
        if self.right is not None:
            output = self.right.post_order(output)
        output = f'{output}{self.data}|'
        return output

