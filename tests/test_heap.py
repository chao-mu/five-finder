from five_finder.heap import Heap

import random
from math import inf

RandomInts = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

def verify_heap_order(heap):
    last_num = -inf
    print("---")
    while not heap.empty():
        num = heap.get()
        print(num)
        #assert num >= last_num
        last_num = num

def test_non_int():
    target = 5
    class NonIntHeap(Heap):
        def less_than(self, a, b):
            return a[-1][0] < b[-1][0]
            #print(target)
            #return abs(a[-1][0] - target) < abs(b[-1][0] - target)


    heap = NonIntHeap()

    n = 10
    xs = [[(i, "bacon")] for i in RandomInts]

    heap.extend(xs)

    last_dist = -inf
    while not heap.empty():
        num = heap.get()[-1][0]
        print(num)
        #dist = abs(target - num)
        #print(f"{num} {dist}")

        #assert dist >= last_dist
        #last_dist = dist

def skip_test_add_get():
    heap = Heap()
    heap.extend(RandomInts)
    verify_heap_order(heap)

def skip_test_middle_get():
    heap = Heap()
    heap.extend(RandomInts)

    heap.get(len(RandomInts) // 2)
    verify_heap_order(heap)
