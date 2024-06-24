def combinationSum(nums, target):
  #we can keep using the same number
  #until the sum equates to target
  #Decision tree with backtracking!

  #backtracking: usually dfs
  #start with base case (we get the result)
  #define branches (what path can we take?)
  #think of cases where we return without doing anything
  #like out of bounds, or for this case the sum is too big
  res = []
  n = len(nums)

  def dfs(i, curr, sum):
    #base case
    if sum == target:
      res.append(curr.copy())
      return
    
    #if too big or OOB, go back
    if i >= n or sum > target:
      return
    
    #backtracking: either add current or next
    curr.append(nums[i])
    dfs(i, curr, sum + nums[i])

    curr.pop()
    dfs(i + 1, curr, sum)
  
  dfs(0, [], 0)

  return res

def main():
  nums = [2, 5, 9]
  res = combinationSum(nums, 9)
  for l in res:
    print(l)
  
  return

if __name__ == "__main__":
  main()