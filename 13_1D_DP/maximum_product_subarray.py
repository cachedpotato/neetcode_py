from typing import List
def maxProduct(nums: List[int]) -> int:
  #if positive: keeps getting bigger
  #if negative: the absolute value keeps getting bigger
  #but alternates between negative and positive
  #if zero: everything zeroes out (skip)
  #max value can be attained either by:
  #current max value * current number
  #current min value (-) * current number (-)
  #current number itself

  res = max(nums)
  currMax, currMin = 1, 1
  for n in nums:
    temp = n * currMax
    currMax = max(n * currMax, n * currMin, n)
    currMin = min(temp, n * currMin, n)
    res = max(currMax, res)
  
  return res

def main():
  nums = [1, 2, -3, 4]
  print("max subarray product: {}".format(maxProduct(nums)))

if __name__ == "__main__":
  main()