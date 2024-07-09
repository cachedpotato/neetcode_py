from typing import List
#Sometimes it's easier to solve the reverse question first
#Then get the answer we want
#in this case: we get the UNSURROUNDED REGIONs first (Mark)
#Then change all the remaining O into X
#And finally revert the marked Os back into O

def surroundingRegions(board: List[List[int]]) -> None:
  numRow = len(board)
  numCol = len(board[0])

  def dfs(row: int, col: int) -> None:
    nonlocal numRow
    nonlocal numCol
    if (row not in range(numRow) or
        col not in range(numCol) or
        board[row][col] != "O"):
      return
    
    board[row][col] = "T"
    dfs(row + 1, col)
    dfs(row - 1, col)
    dfs(row, col + 1)
    dfs(row, col - 1)

  #STEP 1. MARK UNSURROUNDED Os
  for row in range(numRow):
    for col in range(numCol):
      if ((row in [0, numRow - 1] or col in [0, numCol - 1]) and
          board[row][col] == "O"):
        dfs(row, col)
  
  #STEP 2. CHANGE ALL THE SURROUNDED O INTO X
  for row in range(numRow):
    for col in range(numCol):
      if board[row][col] == "O":
        board[row][col] = "X"

  
  #STEP 3: REVERT MARKED O BACK INTO O
  for row in range(numRow):
    for col in range(numCol):
      if board[row][col] == "T":
        board[row][col] = "O"
  
  return


def main():
  board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","O","O","X"],
    ["X","X","X","O"]
  ]
  print("BEFORE")
  for r in board:
    print(r)
  surroundingRegions(board)
  print("AFTER")
  for r in board:
    print(r)

if __name__ == "__main__":
  main()

