from five_finder.heap import Heap

import random

# Ideas: If an edge is involved in a path X times, drop it

class ChaosHeap(Heap):
    def __init__(self, target, chance_random=0):
        self.target = target
        self.chance_random = chance_random

        super().__init__()

    def get(self):
        if random.random() < self.chance_random:
            idx = random.randint(0, self.size - 1)
        else:
            idx = 0

        return super().get(idx)

    def less_than(self, a, b):
        return abs(a[-1][0] - self.target) < abs(b[-1][0] - self.target)
