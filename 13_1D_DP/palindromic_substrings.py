def countSubstrings(s: str) -> int:
  
  def isPalindrome(s: str) -> bool:
    if len(s) < 2:
      return True
    
    l = len(s)
    for i in range(l // 2):
      if s[i] != s[l - 1 - i]:
        return False
    return True
  
  strLen = len(s) 
  l, r = 0, strLen - 1
  c = 0
  res = strLen

  while l < r:
    while r < strLen:
      if isPalindrome(s[l:r+1]):
        res += 1
      l += 1
      r += 1
    
    l = 0
    c += 1
    r = strLen - 1 - c
  
  return res

def main():
  s = "fdsklf"
  r = countSubstrings(s)
  print(r)

if __name__ == "__main__":
  main()