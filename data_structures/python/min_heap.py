class MinHeap:
    """
    MinHeap is a binary tree-like data structure, but uses a list/array to
    store the values In a `MIN` heap, values are always lower than their
    children.  The inverse is true for 'MAX' heap. A heap should always
    be a full/complete binary tree, never open spots in-between values
    For INSERTION, the new item is added in the last available spot and
    heapified UP For DELETION, the root is removed, the last item replaces
    the root and is heapified DOWN Sorting is similar to insertion sort,
    average runtime is O(n log(n))

    Ex.  [10, 15, 18, 16, 17]

                10
              /    \
           15       18
          /  \
        16    17

    """
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.size: int = 0
        self.items: list = [None] * self.capacity

    def __repr__(self):
        return " => ".join(str(x) for x in self.items)

    def peek(self) -> int:
        """
        Find the entry with the minimum value without removing it
        :return: int - the minimum value entry in the items list
        """
        if self.size == 0:
            raise ValueError
        return self.items[0]

    def poll(self) -> int:
        """
        Find the entry with the minimum value and remove it from the heap
        :return: int - the minimum value entry that has been removed
        """
        if self.size == 0:
            raise ValueError
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return item

    def add(self, item: int) -> None:
        """
        Add or insert a new item in the heap at the next available position
        in the tree :param item: int - the item to be added / inserted
        """
        if self.size >= self.capacity:
            # Increase capacity of the items list
            self.capacity += 1
            self.items.append(None)
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_up(self) -> None:
        """
        Arrange the items list into a proper heap, moving from bottom to
        top (e.g. after insertion)
        """
        index = self.size - 1
        while self.has_parent(index) and \
                self.parent(index) > self.items[index]:
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)

    def heapify_down(self) -> None:
        """
        Arrange the items list into a proper heap, moving from top to
        bottom (e.g. after deletion)
        """
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.left_child_index(index)
            if self.has_right_child(index) \
                    and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.right_child_index(index)
            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index

    def swap(self, index_one: int, index_two: int) -> None:
        """
        Swap two positions in the heap given two different indices
        :param index_one: int - the first index to be swapped
        :param index_two: int - the second index to be swapped
        """
        temp = self.items[index_one]
        self.items[index_one] = self.items[index_two]
        self.items[index_two] = temp

    def heap_sort(self) -> None:
        """Sort the heap items list in proper heap order"""
        for index in range(self.size - 1, 0, -1):
            self.swap(0, index)
            self.heapify_down()

    @staticmethod
    def parent_index(child_index: int) -> int:
        """
        Get the parent index of a given child index
        :param child_index: int - index of the child
        :return: int - the parent index
        """
        return (child_index - 1)//2

    @staticmethod
    def left_child_index(parent_index: int) -> int:
        """
        Get the left child index of a given parent index
        :param parent_index: int - the index of the parent
        :return: int - the left child index
        """
        return (2 * parent_index) + 1

    @staticmethod
    def right_child_index(parent_index: int) -> int:
        """
        Get the right child index of a given parent index
        :param parent_index: int - the index of the parent
        :return: int - the right child index
        """
        return (2 * parent_index) + 2

    def has_left_child(self, index: int) -> bool:
        """
        Check if a heap item has a left child, given the
        index of the heap item
        :param index: int - the index to be checked
        :return: bool - whether a left child exists
        """
        return self.left_child_index(index) < self.size

    def has_right_child(self, index: int) -> bool:
        """
        Check if a heap item has a right child, given the
        index of the heap item
        :param index: int - the index to be checked
        :return: bool - whether a right child exists
        """
        return self.right_child_index(index) < self.size

    def has_parent(self, index: int) -> bool:
        """
        Check if a heap item has a parent, given the
        index of the heap item
        :param index: int - the index to be checked
        :return: bool - whether a parent exists
        """
        return self.parent_index(index) >= 0

    def left_child(self, index: int) -> int:
        """
        Get the left child of a given index
        :param index: int - the index to be checked
        :return: int - the left child of the given index
        """
        return self.items[self.left_child_index(index)]

    def right_child(self, index: int) -> int:
        """
        Get the right child of a given index
        :param index: int - the index to be checked
        :return: int - the right child of the given index
        """
        return self.items[self.right_child_index(index)]

    def parent(self, index: int) -> int:
        """
        Get the parent of a given index
        :param index: int - the index to be checked
        :return: int - the parent of the given index
        """
        return self.items[self.parent_index(index)]


if __name__ == '__main__':
    heap = MinHeap(5)
    heap.add(6)
    heap.add(4)
    heap.add(14)
    heap.add(1)
    print(heap)
