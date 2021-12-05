from five_finder.structs import ChaosHeap

import random
from math import inf

def verify_heap_order(heap):
    last_num = -inf
    while not heap.empty():
        num = heap.get()
        assert num >= last_num
        last_num = num

def test_ChaosHeap_less_than():
    target = 5
    less_than = lambda a, b: abs(a[-1][0] - target) < abs(b[-1][0] - target)
    n = 10
    xs = [[(i, "bacon")] for i in range(n)]
    random.shuffle(xs)

    heap = ChaosHeap(less_than=less_than)
    heap.extend(xs)

    last_dist = -inf
    while not heap.empty():
        num = heap.get()[-1][0]
        dist = abs(target - num)
        assert dist >= last_dist
        last_dist = dist

def test_ChaosHeap():
    xs = list(range(10)) * 3
    random.shuffle(xs)

    heap = ChaosHeap()
    heap.extend(xs)
    verify_heap_order(heap)

    xs = list(range(10))
    random.shuffle(xs)

    heap = ChaosHeap()
    heap.extend(xs)
    heap.get(len(xs) // 2)
    verify_heap_order(heap)
