def climbStairs(n: int) -> int:
  #classic DP
  #The crux of DP: Breaking things down into subproblems
  #Can be BOTTOM UP or TOP DOWN
  #NEED MORE DATA BUT FEELS LIKE MAX: TOP DOWN / MIN: BOTTOM UP

  #How to break down into subproblems?
  #after defining base cases,
  #given problem p(n) try to create a formula between
  #p(n), p(n-1), p(n - 2)...
  #normally need some sort of iteration + adding to previous result
  #to get final answer

  #CLIMBING STAIRS
  #can move only 1 or 2 stairs at a time
  #at stair i < n - 3:
  #we can go up 1 stair OR go up 2 stairs
  #stairs(i) = stairs(i + 1) + stairs(i + 2)

  if n < 3:
    return n
  
  #[.....curr, n2, n1(stair n)]
  n2 = 2
  n1 = 1
  for _ in range(n - 3, -1, -1):
    temp = n2 + n1
    #move down: [.......curr,n2, n1], stair n]
    n1 = n2
    n2 = temp
  
  return n2





  pass
def main():
  print(climbStairs(4))

if __name__ == "__main__":
  main()

  