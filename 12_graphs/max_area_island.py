from typing import List
from collections import deque

def maxAreaOfIsland(grid: List[List[int]]) -> int:
  #pretty much the same as number of islands
  #just the return value is different
  #for some reason I still cannot solve this without encountering
  #any bugs because I KEEP FOGETTING TO ADD THE VISITED CONDITION
  #I'M DOING THIS OVER AND OVER AGAIN TILL IT GETS DRILLED INTO MY GODDAMN HEAD

  if not grid: return 0
  numRow = len(grid)
  numCol = len(grid[0])
  maxArea = 0
  visited = set()

  def bfs(r: int, c: int) -> int:
    #return area of island
    nonlocal numCol
    nonlocal numRow
    q = deque()
    q.append((r, c))
    visited.add((r, c))
    area = 1

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
      currRow, currCol = q.popleft()
      for dr, dc in directions:
        newRow, newCol = currRow + dr, currCol + dc
        if (newRow in range(numRow) and
            newCol in range(numCol) and
            (newRow, newCol) not in visited and
            grid[newRow][newCol] == 1):
          
          q.append((newRow, newCol))
          visited.add((newRow, newCol))
          area += 1
      
    return area
  
  for row in range(numRow):
    for col in range(numCol):
      if grid[row][col] == 1 and (row, col) not in visited:
        maxArea = max(maxArea, bfs(row, col))

  return maxArea

def main():
  grid = [
    [0,1,1,0,1],
    [1,0,1,0,1],
    [0,1,1,0,1],
    [0,1,0,0,1]
  ]

  print("max area of island: {}".format(maxAreaOfIsland(grid)))

if __name__ == "__main__":
  main()