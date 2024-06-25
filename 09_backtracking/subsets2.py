def subsetsWithDup(nums):
  #subsets with duplicates
  #we need some sort of way to track duplicates
  #I chose to use hash at the cost of memory
  #sorting the list can also work

  l = len(nums)
  res = []
  curr = []
  resHashList = [] #list of count hash for each element in res

  def backtrack(i: int) -> None:
    if i >= l:
      countHash = {}
      for n in curr:
        countHash[n] = countHash.get(n, 0) + 1
      if countHash in resHashList:
        return
      resHashList.append(countHash)
      res.append(curr.copy())
      return
    
    curr.append(nums[i])
    backtrack(i + 1)
    curr.pop()
    backtrack(i + 1)
  
  backtrack(0)
  return res

def subsetsWithDupSort(nums):
  #sorting variant
  res = []
  nums.sort()
  l = len(nums)

  def backtrack(i, subset):
    if i == len(nums):
      res.append(subset[::])
      return
    
    #either add the current number (same number)
    subset.append(nums[i])
    backtrack(i + 1, subset)

    #or add a different number
    subset.pop()
    while i + 1 < l and nums[i] == nums[i + 1]:
      i += 1
    backtrack(i + 1, subset)
  
  backtrack(0, [])
  return res

def main():
  nums = [1, 2, 1]
  print("[{}]".format(", ".join(["{}".format(l) for l in subsetsWithDup(nums)])))
  print("[{}]".format(", ".join(["{}".format(l) for l in subsetsWithDupSort(nums)])))


if __name__ == "__main__":
  main()