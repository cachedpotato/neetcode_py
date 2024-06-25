def letterCombinations(digits: str):
  numToAlphaList = [[]] * 10
  numToAlphaList[2] = ["a", "b", "c"]
  numToAlphaList[3] = ["d", "e", "f"]
  numToAlphaList[4] = ["g", "h", "i"]
  numToAlphaList[5] = ["j", "k", "l"]
  numToAlphaList[6] = ["m", "n", "o"]
  numToAlphaList[7] = ["p", "q", "r", "s"]
  numToAlphaList[8] = ["t", "u", "v"]
  numToAlphaList[9] = ["w", "x", "y", "z"]

  length = len(digits)
  res = []
  def backTrack(i, curr):
    nonlocal length
    if i >= length:
      res.append("".join(ch for ch in curr))
      return
    
    n = int(digits[i])
    for charOptions in numToAlphaList[n]:
      curr.append(charOptions)
      backTrack(i + 1, curr)
      curr.pop()
    
  
  backTrack(0, [])
  return res

def letterCombinationsOptimized(digits: str):
  #an optimized version of the solution above
  #we really don't need the curr list, just add string directly
  #the stack insert/pop is intuitive, but we can remove all and just
  #go straight to backtracking if we do not add to curr  in the first placea

  numToAlphaList = [""] * 10
  numToAlphaList[2] = "abc"
  numToAlphaList[3] = "def"
  numToAlphaList[4] = "ghi"
  numToAlphaList[5] = "jkl"
  numToAlphaList[6] = "mno"
  numToAlphaList[7] = "pqrs"
  numToAlphaList[8] = "tuv"
  numToAlphaList[9] = "wxyz"

  res = []
  length = len(digits)
  def backtrack(i, currStr):
    nonlocal length
    if i >= length:
      res.append(currStr)
      return
    
    n = int(digits[i])
    for ch in numToAlphaList[n]:
      backtrack(i + 1, currStr + ch)
  
  backtrack(0, "") 
  return res




def main():
  digits = "34"
  print("{}".format(", ".join(["\"{}\"".format(r) for r in letterCombinations(digits)])))
  print("{}".format(", ".join(["\"{}\"".format(r) for r in letterCombinationsOptimized(digits)])))

if __name__ == "__main__":
  main()