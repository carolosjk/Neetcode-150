from typing import List

class Heap:
    def __init__(self, arr: List[int]=None):
        if not arr:
            self.heap = []
        else:
            self.heap = arr
            self._heapify()

    def _heapify(self):
        n = len(self.heap)
        for i in range(n//2 -1, -1, -1):
            self._sift_down(i)

    def _sift_down(self, i: int):
        n = len(self.heap)
        smallest = i
        left = 2*i+1
        right = 2*i+2

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._sift_down(smallest)

    def _sift_up(self, i: int):
        while i > 0:
            parent = (i-1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
        
    def push(self, val: int):
        self.heap.append(val)
        self._sift_up(len(self.heap)-1)

    def pop(self):
        if not self.heap:
            raise IndexError("Tried to pop from empty heap")
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return top
    
    def peek(self):
        if not self.heap:
            raise IndexError("Tried to pop from empty heap")
        return self.heap[0]
    
    def __len__(self):
        return len(self.heap)
    
    def __str__(self):
        return str(self.heap)

if __name__ == "__main__":
    heap = Heap()
    print(len(heap))
    print(heap.push(10))
    print(heap.push(5))
    print(heap.push(3))
    print(heap.push(4))
    print(heap.push(5))
    print(heap.push(134))
    print(heap.push(23))
    print(heap.peek())
    print(heap.pop())
    print(heap.peek())