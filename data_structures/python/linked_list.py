from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def append(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data: Any) -> None:
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def add_after(self, target_data: Any, new_data: Any) -> None:
        if not self.head:
            raise Exception("List is empty")
        current = self.head
        while current.next is not None:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def add_before(self, target_data: Any, new_data: Any) -> None:
        if not self.head:
            raise Exception("List is empty")
        current = self.head
        while current.next is not None:
            if current.next.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_with_value(self, data: Any) -> None:
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.append("a")
    llist.append("b")
    llist.append("c")
    llist.append("d")
    llist.append("f")
    print(llist)
    llist.delete_with_value("c")
    print(llist)
    llist.add_after("b", "c")
    print(llist)
    llist.delete_with_value("d")
    print(llist)
    llist.add_before("f", "d")
    print(llist)
