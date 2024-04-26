class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) -1
        self.bubble_up(index)

    def bubble_up(self, index):
        parent_index = index - 1
        if parent_index>=0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.bubble_up(parent_index)


    def get_min(self):
        return self.heap[0]

    def get_heap(self):
        return self.heap



heap = MinHeap()
heap.insert(3)

heap.insert(2)
heap.insert(7)
heap.insert(1)
heap.insert(18)
heap.insert(5)
print("JJ---",heap.get_min())
print(heap.get_heap())