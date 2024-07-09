from collections import deque
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    numRow = len(grid)
    numCol = len(grid[0])
    #we don't need visited set for once because
    #we will change the grid as we go in such a way that
    #makes visited cells unviable for next search
    q = deque()
    fresh = 0
    time = 0

    #get all the rotten oranges
    for row in range(numRow):
        for col in range(numCol):
            if grid[row][col] == 1:
                fresh += 1
            if grid[row][col] == 2:
                q.append((row, col))

    
    #do bfs search for all rotten fruit
    #we will be bf searching for all rotten fruits AT THE SAME TIME
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q and fresh > 0:
        time += 1
        for _ in range(len(q)):
            currRow, currCol = q.popleft()
            for dr, dc in directions:
                newRow, newCol = currRow + dr, currCol + dc
                if (newRow in range(numRow) and
                    newCol in range(numCol) and
                    grid[newRow][newCol] == 1):
                    grid[newRow][newCol] = 2
                    fresh -= 1
                    q.append((newRow, newCol))
    
    return time if fresh == 0 else -1 

def main():
    grid=[[2,1,1],[1,1,0],[0,1,1]]
    a = orangesRotting(grid)
    print(a)

if __name__ == "__main__":
    main()