class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        # print("AN", self.heap)
        if len(self.heap) > 1:
            self.bubble_up(self.heap)

    def get_heap(self):
        return self.heap


    def bubble_up(self, heap):

        is_even = len(heap) % 2
        last_index = len(heap) - 1
        # print("heap", heap)
        if(is_even == 0):
            p = int((last_index - 1)/2)
        else:
            p = int((last_index - 2)/2)
        # print("Before swap",self.heap)
        # print("P", p)
        if (self.heap[p] > self.heap[last_index]):
            self.heap[p], self.heap[last_index] = self.heap[last_index], self.heap[p]

        # if(is_even !=0 and self.heap[last_index] < self.heap[last_index -1]):
        #     self.heap[last_index], self.heap[last_index -1] = self.heap[last_index-1], self.heap[last_index]


        # print("After swap",self.heap)

        if (len(heap[:-1]) > 1 ):
            # print("New",heap[:-1])
            self.bubble_up(heap[:-1])


    # def deleteMin(self):
    #     self.heap.pop(0)
    #     if len(self.heap) > 1:
    #         self.bubble_up(self.heap)




heap = BinaryHeap()
heap.insert(19)

heap.insert(6)
heap.insert(8)

heap.insert(11)
heap.insert(4)
heap.insert(5)

print("JJ---",heap.get_heap())
heap.deleteMin()
print("JJ---",heap.get_heap())
# r = [2,3,4,5]
#
# print(r[:-1])
