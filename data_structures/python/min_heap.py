class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.items = [None] * self.capacity

    def parent_index(self, child_index):
        return child_index//2

    def left_child_index(self, parent_index):
        return 2 * parent_index

    def right_child_index(self, parent_index):
        return (2 * parent_index) + 1

    def has_left_child(self, parent_index):
        return self.left_child_index(parent_index) < self.size

    def has_right_child(self, index):
        return self.right_child_index(index) < self.size

    def has_parent(self, index):
        return self.parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.left_child_index(index)]

    def right_child(self, index):
        return self.items[self.right_child_index(index)]

    def parent(self, index):
        return self.items[self.parent_index(index)]

    def swap(self, index_one, index_two):
        temp = self.items[index_one]
        self.items[index_one] = self.items[index_two]
        self.items[index_two] = temp

    def peek(self):
        if self.size == 0:
            raise ValueError
        return self.items[0]

    def poll(self):
        if self.size == 0:
            raise ValueError
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return item

    def add(self, item):
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)
