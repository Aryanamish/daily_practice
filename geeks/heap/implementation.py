import heapq


class MaxHeap:

    def __init__(self):
        self.heap = []

    def append(self, x):
        parent = lambda x: (x - 1) // 2
        heap = self.heap
        heap.append(x)
        n = len(heap) - 1
        p = parent(n)
        while p >= 0 and heap[p] < heap[n]:
            heap[n], heap[p] = heap[p], heap[n]
            n = p
            p = parent(p)

    def peek(self):
        return self.heap[0]

    def push_pop(self, x):
        heap = self.heap
        pop = heapq._heappop_max(heap) if len(heap) > 0 else None
        self.append(x)
        return pop

    def __repr__(self):
        return str(self.heap)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, index):
        return self.heap[index]


class MinHeap:

    def __init__(self):
        self.heap = []

    def append(self, x):
        heapq.heappush(self.heap, x)

    def peek(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def push_pop(self, x):
        val = self.heap[0] if len(self.heap) > 0 else None
        heapq.heapreplace(self.heap, x)
        return val

    def pop(self):
        return heapq.heappop(self.heap) if len(self.heap) > 0 else None

    def __repr__(self):
        return str(self.heap)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, index):
        return self.heap[index]
