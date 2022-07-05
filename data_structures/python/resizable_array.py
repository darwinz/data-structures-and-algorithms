# resizable array data structure implementation
class ResizableArray:
    def __init__(self):
        self.array = []
        self.size = 0
        self.capacity = 0
        self.load_factor = 0.75

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.array)

    def __str__(self):
        return str(self.array)

    def append(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def remove(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                if self.size < self.capacity * self.load_factor:
                    self.resize(self.capacity // 2)

    def pop(self, index):
        value = self.array[index]
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        if self.size < self.capacity * self.load_factor:
            self.resize(self.capacity // 2)
        return value

    def clear(self):
        self.array = []
        self.size = 0
        self.capacity = 0

    def index(
        self, value, start=0, end=None,
        error_message="Value not found in resizable array"
    ):
        if end is None:
            end = self.size
        for i in range(start, end):
            if self.array[i] == value:
                return i
        raise ValueError(error_message)
