from unittest import TestCase

from data_structures.python.min_heap import MinHeap


class TestMinHeap(TestCase):
    def setUp(self):
        self.min_heap = MinHeap(5)

    def test_peek_should_return_lowest_item(self):
        self.min_heap.add(4)
        self.min_heap.add(2)
        self.min_heap.add(7)
        self.assertEqual(2, self.min_heap.peek())

    def test_poll_should_remove_the_min_item_and_heapify(self):
        self.min_heap.add(4)
        self.min_heap.add(14)
        self.min_heap.add(6)
        self.min_heap.add(7)
        self.min_heap.poll()
        self.assertEqual(6, self.min_heap.items[0])

    def test_add_more_than_allocated_should_resize_dynamically(self):
        self.min_heap.items = [4, 6, 11, 7, 14]
        self.min_heap.size = len(self.min_heap.items)
        self.min_heap.add(3)
        self.assertEqual(6, len(self.min_heap.items))

    def test_heapify_up_should_arrange_heap_properly(self):
        self.min_heap.items = [5, 13, 24, 16, 7]
        self.min_heap.size = len(self.min_heap.items)
        self.min_heap.heapify_up()
        self.assertEqual(7, self.min_heap.items[1])

    def test_heapify_down_should_arrange_heap_properly(self):
        self.min_heap.items = [16, 13, 24]
        self.min_heap.size = len(self.min_heap.items)
        self.min_heap.heapify_down()
        self.assertEqual(13, self.min_heap.items[0])

    def test_swap_should_swap_two_items(self):
        self.min_heap.items = [50, 10, 13, 14, 21, 26, 8]
        self.min_heap.size = len(self.min_heap.items)
        self.min_heap.swap(0, self.min_heap.size - 1)
        self.assertEqual(8, self.min_heap.items[0])

    def test_heap_sort_should_sort_list_into_proper_heap(self):
        self.min_heap.items = [50, 5, 13, 1, 21, 45, 8]
        self.min_heap.size = len(self.min_heap.items)
        self.min_heap.heap_sort()
        self.assertEqual([1, 8, 5, 45, 21, 13, 50], self.min_heap.items)

    def test_parent_index_returns_floor_of_half_child_index(self):
        subject = 3
        self.assertEqual(1, self.min_heap.parent_index(subject))

    def test_left_child_index_returns_double_parent_index_plus_one(self):
        subject = 4
        self.assertEqual(9, self.min_heap.left_child_index(subject))

    def test_right_child_index_returns_double_parent_index_plus_two(self):
        subject = 4
        self.assertEqual(10, self.min_heap.right_child_index(subject))

    def test_has_left_child_returns_bool(self):
        self.min_heap.items = [5, 13, 24, 16, 7]
        self.min_heap.size = len(self.min_heap.items)
        self.assertFalse(self.min_heap.has_left_child(2))
        self.assertTrue(self.min_heap.has_left_child(1))

    def test_has_right_child_returns_bool(self):
        self.min_heap.items = [5, 13, 24, 16]
        self.min_heap.size = len(self.min_heap.items)
        self.assertFalse(self.min_heap.has_right_child(1))
        self.assertTrue(self.min_heap.has_right_child(0))

    def test_has_parent_returns_bool(self):
        self.min_heap.items = [5, 13, 24, 16, 7]
        self.min_heap.size = len(self.min_heap.items)
        self.assertTrue(self.min_heap.has_parent(1))
        self.assertTrue(self.min_heap.has_parent(4))

    def test_left_child_returns_left_child(self):
        self.min_heap.items = [5, 13, 24, 16]
        self.min_heap.size = len(self.min_heap.items)
        self.assertEqual(16, self.min_heap.left_child(1))

    def test_right_child_returns_right_child(self):
        self.min_heap.items = [5, 13, 24, 16, 7]
        self.min_heap.size = len(self.min_heap.items)
        self.assertEqual(7, self.min_heap.right_child(1))

    def test_parent(self):
        self.min_heap.items = [5, 13, 24, 16, 7]
        self.min_heap.size = len(self.min_heap.items)
        self.assertEqual(13, self.min_heap.parent(4))
