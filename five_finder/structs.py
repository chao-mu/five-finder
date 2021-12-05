class ChaosHeap:

    def __init__(self, less_than=None):
        if less_than is None:
            less_than = lambda a, b: a < b

        self.less_than = less_than
        self.items = []
        self.size = 0

        # TODO: Make these functions of size of heap
        #self.should_drop_heap =
        #self.should_drop_seen =
        #self.should_random_select =

    def left_child_idx(self, idx):
        return idx * 2 + 1

    def left_child(self, idx):
        idx = self.left_child_idx(idx)
        return idx, self.items[idx]

    def right_child(self, idx):
        idx = self.left_child_idx(idx) + 1
        return idx, self.items[idx]

    def has_child(self, idx):
        return self.items[self.left_child_idx(idx)] is not None

    def parent_idx(self, idx):
        return idx // 2

    def has_parent(self, idx):
        return self.items[self.parent_idx(idx)] is not None

    def ensure_space(self):
        diff = self.size * 2 - len(self.items)
        if diff > 0:
            self.items += [None] * diff

    def empty(self):
        return self.size == 0

    def swap(self, i, j):
        self.items[i], self.items[j] = (self.items[j], self.items[i])

    def get(self, idx=None):
        if self.empty():
            return None

        if idx is None:
            idx = 0

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
            parent_idx = self.parent_idx(idx)
            if not self.less_than(self.items[idx], self.items[parent_idx]):
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

            if self.less_than(self.items[idx], self.items[smallest_idx]):
                break

            self.swap(idx, smallest_idx)
            idx = smallest_idx
