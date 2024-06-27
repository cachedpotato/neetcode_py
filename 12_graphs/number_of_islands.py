from typing import List
from collections import deque
def numIslands(grid: List[List[int]]) -> int:
  #One of the most important graph questions
  #graph search: either by dfs or bfs
  #in this case bfs seems more intuitive
  #we need to keep track of visited coordinates -> have a set
  if not grid:
    return 0
  
  numRow = len(grid) 
  numCol = len(grid[0])
  islands = 0
  visited = set()

  #bfs is used mainly for figuring out islands
  #and updating the visited set
  def bfs(r: int, c: int) -> None:
    nonlocal numRow
    nonlocal numCol

    q = deque()
    q.append((r, c))
    visited.add((r, c))

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
      currRow, currCol = q.popleft()
      for dr, dc in directions:
        newRow, newCol = currRow + dr, currCol + dc
        if (newRow in range(numRow) and
            newCol in range(numCol) and
            (newRow, newCol) not in visited and
            grid[newRow][newCol] == "1"):
          
          q.append((newRow, newCol))
          visited.add((newRow, newCol))
    
    return

  for row in range(numRow):
    for col in range(numCol):
      if grid[row][col] == "1" and (row, col) not in visited:
        bfs(row, col)
        islands += 1

  return islands

def numIslands_dfs(grid: List[List[int]]) -> int:
  #dfs variant of the same question
  if not grid:
    return 0
  
  numRow = len(grid) 
  numCol = len(grid[0])
  islands = 0
  visited = set()

  #bfs is used mainly for figuring out islands
  #and updating the visited set
  def dfs(r: int, c: int) -> None:
    nonlocal numRow
    nonlocal numCol

    currCoord = (r, c)
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for dr, dc in directions:
      newRow, newCol = currCoord[0] + dr, currCoord[1] + dc
      if (newRow in range(numRow) and
          newCol in range(numCol) and
          grid[newRow][newCol] == "1" and
          (newRow, newCol) not in visited):
        
        visited.add((newRow, newCol))
        dfs(newRow, newCol)

    
    return

  for row in range(numRow):
    for col in range(numCol):
      if grid[row][col] == "1" and (row, col) not in visited:
        dfs(row, col)
        islands += 1

  return islands

def main():
  grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

  print("number of islands: {}".format(numIslands(grid)))
  print("number of islands: {}".format(numIslands_dfs(grid)))

if __name__ == "__main__":
  main()