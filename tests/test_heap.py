from five_finder.heap import Heap

import random
from math import inf

RandomInts = tuple(reversed(range(14)))

def verify_heap_order(heap):
    last_num = -inf
    #print("---")
    while not heap.empty():
        num = heap.get()
        assert num >= last_num
        last_num = num

def verify_heap_invariant(heap, less_than=None):
    if less_than is None:
        less_than = lambda a, b: a < b

    items = heap.items
    for idx in range(heap.size):
        item = items[idx]
        left_child = items[idx * 2 + 1]
        right_child = items[idx * 2 + 2]

        assert left_child is None or not less_than(left_child, item)
        assert right_child is None or not less_than(right_child, item)

def extend(heap, items, less_than=None):
    for item in items:
        heap.put(item)
        verify_heap_invariant(heap, less_than=less_than)

def test_non_int():
    target = 5
    less_than = lambda a, b: abs(a[-1][0] - target) < abs(b[-1][0] - target)
    class NonIntHeap(Heap):
        def less_than(self, a, b):
            return less_than(a, b)

    heap = NonIntHeap()
    xs = [[(i, None)] for i in RandomInts]
    extend(heap, xs, less_than=less_than)

    n = 10

    last_dist = -inf
    while not heap.empty():
        num = heap.get()[-1][0]
        dist = abs(num - target)
        assert dist >= last_dist
        last_dist = dist

def test_add_get():
    heap = Heap()
    verify_heap_order(heap)
    verify_heap_invariant(heap)

def test_middle_get():
    heap = Heap()
    heap.extend(RandomInts)

    heap.get(len(RandomInts) // 2)
    verify_heap_invariant(heap)
    verify_heap_order(heap)
