import heapq
class KthLargest:
  #kth largest > Heap. No questions asked.
  #why min heap? if we have a min heap of size k,
  #the kth largest element is actually the smallest element
  #in the min heap, which is the root.

  def __init__(self, k: int, nums) -> None:
    self.minHeap = nums
    self.k = k
    heapq.heapify(self.minHeap)

    while len(self.minHeap) > self.k:
      heapq.heappop(self.minHeap)

  def add(self, val: int) -> int:
    #update min heap
    heapq.heappush(self.minHeap, val)
    while len(self.minHeap) > self.k:
      heapq.heappop(self.minHeap)
    
    return self.minHeap[0]


def main():
  k = 3
  stream = [1, 2, 3, 3]
  kthlargest = KthLargest(k, stream)
  print(kthlargest.add(3))
  print(kthlargest.add(5))
  print(kthlargest.add(6))
  print(kthlargest.add(7))
  print(kthlargest.add(8))

if __name__ == "__main__":
  main()