def exist(board, word: str) -> bool:
  startchar = word[0]
  numRow = len(board)
  numCol = len(board[0])
  possibleStart = []
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == startchar:
        possibleStart.append((i, j))
  
  if len(possibleStart) == 0: return False

  res = False
  def backtrack(start, currentPath, currentWord):
    nonlocal numRow
    nonlocal numCol
    nonlocal res
    if currentWord == word:
      res = True
      return
      
    if len(currentPath) > len(word):
      return
      
      #given(i, j), possible movements:
      #(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)
    for direction in [(start[0], start[1] + 1), (start[0], start[1] - 1), (start[0] + 1, start[1]), (start[0] - 1, start[1])]:
      if direction not in currentPath and -1 < direction[0] < numRow and -1 < direction[1] < numCol:
        currentPath.append(direction)
        backtrack(direction, currentPath, currentWord + board[direction[0]][direction[1]])
        currentPath.pop()
  
  for s in possibleStart:
    backtrack(s, [s], startchar)
    if res == True: return True
  
  return False

def main():
  board = [
    ["A","B","C","D"],
    ["S","A","A","T"],
    ["A","C","A","E"]
  ]
  word = "CAT"

  print(exist(board, word))
  test = "test"
  print(test[0:0])

if __name__ == "__main__":
    main()