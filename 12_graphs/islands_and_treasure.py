from typing import List
from collections import deque
#islands question but now we have to update distance from each level
#remember this?
#while q:
#  currLevel += 1
#  for i in range(len(q)):
#    curr = q.popleft()
#    ...
#we need this extra for loop now
#reminder that level-related constants should be
#ABOVE THE FOR LOOP

def islandAndTreasure(grid: List[List[int]]) -> None:
  if not grid: return [[]]
  numRow = len(grid)
  numCol = len(grid[0])
  visited = set()

  #update distance
  #and find path
  def bfs(row: int, col: int) -> None:
    nonlocal numRow
    nonlocal numCol
    q = deque()
    q.append((row, col))
    visited.add((row, col))

    distanceFromTreasure = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while q:
      #level related constant
      distanceFromTreasure += 1
      for _ in range(len(q)):
        currRow, currCol = q.popleft()
        for dr, dc in directions:
          newRow, newCol = currRow + dr, currCol + dc
          if (newRow in range(numRow) and
              newCol in range(numCol) and
              (newRow, newCol) not in visited and
               grid[newRow][newCol] > 0): #DO NOT CHANGE 0
            
            q.append((newRow, newCol))
            visited.add((newRow, newCol))
            #update distance
            grid[newRow][newCol] = min(grid[newRow][newCol], distanceFromTreasure)

    return

  #main logic
  for row in range(numRow):
    for col in range(numCol):
      if grid[row][col] == 0 and (row, col) not in visited:
        bfs(row, col)
        #we need to reset the visited set for
        #other treasures
        visited = set()
  
  return

def main():
  grid = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
  ]

  islandAndTreasure(grid)
  print("{}".format("\n".join(["{}".format(r) for r in grid])))

if __name__ == "__main__":
  main()