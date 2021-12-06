from five_finder.heap import Heap

class ChaosHeap(Heap):
    def __init__(self, target):
        self.target = target

        super().__init__()

    def less_than(self, a, b):
        return abs(a[-1][0] - self.target) < abs(b[-1][0] - self.target)
