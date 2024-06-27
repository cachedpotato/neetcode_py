def numDecodings(s: str) -> int:
  #Use DP Cache
  #using the cache, we will get the previous or next subproblem's
  #result
  #keep going up/down till we reach the end

  #base case: length 0
  dpCache = {len(s): 1}
  #go from the last char to the first (bottom up)
  #at a given position i:
  #dp[i] if we choose to use one digit
  #> 0 if dp[i] == 0 else dp[i + 1] (just grab the next)
  #if we choose to use two digits (s[i:i+2]):
  #we need to check if this is in the range of 1~26
  #if true: add dp[i+2] to dp[i] as well

  #[.....[i], i+1, i+2, ...] or [....., [i, i+1], i+2, ....]
  for i in range(len(s) - 1, -1, -1):
    #choose one digit
    if s[i] == 0:
      dpCache[i] = 0
    else:
      dpCache[i] = dpCache[i + 1]
    
    #choose two digits
    if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
      dpCache[i] += dpCache[i + 2]
    
  return dpCache[0]

def main():
  s = "121"
  print(numDecodings(s))

if __name__ == "__main__":
  main()