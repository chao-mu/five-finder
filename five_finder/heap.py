class Heap:

    def __init__(self):
        self.items = []
        self.size = 0

    def less_than(self, a, b):
        return a < b

    def parent(self, child_idx):
        idx = (child_idx - 1) // 2
        if idx < 0:
            return None, None

        return idx, self.items[idx]

    def left_child(self, parent_idx):
        idx = parent_idx * 2 + 1
        return idx, self.items[idx]

    def right_child(self, parent_idx):
        idx = parent_idx * 2 + 2
        return idx, self.items[idx]

    def has_child(self, idx):
        if idx >= self.size:
            return False

        _, val = self.left_child(idx)
        return val is not None

    def has_parent(self, idx):
        if idx == 0:
            return False

        _, val = self.parent(idx)
        return val is not None

    def ensure_space(self):
        diff = self.size * 2 + 1 - len(self.items)
        if diff > 0:
            self.items += [None] * diff

    def empty(self):
        return self.size == 0

    def swap(self, i, j):
        self.items[i], self.items[j] = (self.items[j], self.items[i])

    def get(self, idx=0):
        item = self.items[idx]
        self.size -= 1
        self.items[idx] = self.items[self.size]
        self.items[self.size] = None
        self.sink(idx)
        self.swim(idx)

        return item

    def extend(self, items):
        for item in items:
            self.put(item)

    def put(self, item):
        self.size += 1
        self.ensure_space()

        idx = self.size - 1
        self.items[idx] = item

        self.swim(idx)

    def swim(self, idx):
        while self.has_parent(idx):
            parent_idx, parent_v = self.parent(idx)
            if self.less_than(parent_v, self.items[idx]):
                break

            self.swap(parent_idx, idx)
            idx = parent_idx

    def sink(self, idx):
        while self.has_child(idx):
            left_idx, left_v = self.left_child(idx)
            right_idx, right_v = self.right_child(idx)
            if right_v is not None and self.less_than(right_v, left_v):
                smallest_idx = right_idx
            else:
                smallest_idx = left_idx

            smallest_v = self.items[smallest_idx]

            if self.less_than(self.items[idx], smallest_v):
                break

            self.swap(idx, smallest_idx)
            idx = smallest_idx

