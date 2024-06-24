import heapq

def lastStoneWeight(stones) -> int:
  #given a list of stones,
  #pick 2 heaviest stones and mash them
  #calculate new weight and push back to the array if not 0

  #need to keep track of 2 biggest: max heap!
  #min heap to max heap > multiply -1!

  stones = [-s for s in stones]
  heapq.heapify(stones) 

  while len(stones) > 1:
    stone1 = heapq.heappop(stones)
    stone2 = heapq.heappop(stones)

    #stone1 heavier than stone2 > abs(stone1) > abs(stone2)
    if stone1 - stone2 < 0:
      heapq.heappush(stones, stone1 - stone2)
  
  return -stones[0] if stones else 0 #make sure to un-multiply -1

def main():
  stones = [2, 3, 6, 2, 4]
  print(lastStoneWeight(stones))

if __name__ == "__main__":
  main()