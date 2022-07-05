# array list data structure implementation
class ArrayList:
    def __init__(self):
        self.array = []

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        return iter(self.array)

    def __str__(self):
        return str(self.array)

    def append(self, value):
        self.array.append(value)

    def insert(self, index, value):
        self.array.insert(index, value)

    def remove(self, value):
        self.array.remove(value)

    def pop(self, index):
        return self.array.pop(index)

    def clear(self):
        self.array.clear()

    def index(self, value):
        return self.array.index(value)

    def count(self, value):
        return self.array.count(value)

    def reverse(self):
        self.array.reverse()

    def sort(self):
        self.array.sort()

    def copy(self):
        return self.array.copy()

    def extend(self, other):
        self.array.extend(other)

    def __add__(self, other):
        return self.array + other

    def __iadd__(self, other):
        self.array += other
        return self

    def __mul__(self, other):
        return self.array * other

    def __imul__(self, other):
        self.array *= other
        return self

    def __rmul__(self, other):
        return self.array * other

    def __eq__(self, other):
        return self.array == other

    def __ne__(self, other):
        return self.array != other

    def __lt__(self, other):
        return self.array < other

    def __le__(self, other):
        return self.array <= other
