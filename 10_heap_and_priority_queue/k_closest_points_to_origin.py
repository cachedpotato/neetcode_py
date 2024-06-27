import heapq
#I HATE MYSELF
def KClosest(points, k):
  minHeap = []
  for x, y in points:
    dist = (x ** 2) + (y ** 2)
    minHeap.append((x, y, dist))
  
  res = []
  for _ in range(k):
    x, y, _ = heapq.heappop(minHeap)
    res.append((x, y))
  
  return res

def main():
  points = [[0, 2], [2, 0], [2, 2]]
  k = 2
  print("[{}]".format(", ".join(["{}".format(r) for r in KClosest(points, k)])))


if __name__ == "__main__":
  main()
    


  