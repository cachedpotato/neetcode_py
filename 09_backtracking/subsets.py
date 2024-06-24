def subsets(nums):
  #GET ALL SUBSETS
  #There are 2^n subsets for an array of size n
  #each element has the choice of either being in the subset or not.
  #This can be interpreted as a depth n tree with 2 branches at each levvel
  #Backtracking in binary tree > dfs

  res = []
  curr = []
  n = len(nums)
  def dfs(i):
    if i >= n:
      #At the end of decision tree
      #append current path to result and return
      res.append(curr.copy())
      return
    
    #two choices: include current number or dont
    #case 1: we add the number to the subset
    curr.append(nums[i])
    #move to next level - recursion
    dfs(i + 1)
    #case 2: we don't add to the subset
    curr.pop()
    dfs(i + 1)
  
  dfs(0)
  return res

def main():
  nums = [1, 2, 3]
  result = subsets(nums) 
  for l in result:
    print(l)


if __name__ == "__main__":
  main()