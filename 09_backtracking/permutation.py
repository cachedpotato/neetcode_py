def permute(nums):
  #to get all possible permutation
  #we need some sort of backtracking mechanism
  #that also tracks the remaining elements left to use

  res = []
  curr = []

  def backtrack(remaining):
    #base case
    if len(remaining) <= 0:
      res.append(curr.copy())
      return
    
    #main logic
    for i in range(len(remaining)):
      #need to iterate over all values in array
      #ORDER MATTERS
      #REMINDER: WHAT GOES IT MUST COME OUT AFTER BACKTRACK
      #AND VICE VERSA
      #Branch: either we add the value at current index or not

      temp = remaining[i]
      #case 1: we add the value
      curr.append(remaining[i])
      del remaining[i]

      backtrack(remaining)

      #case 2: we dont
      #revert remaining and curr array to how it was before
      remaining[i:i] = [temp]
      curr.pop()
    
  backtrack(nums)
  return res

def main():
  nums = [1, 2, 3, 4]
  perms = permute(nums)
  #c = "["
  #for p in perms:
  #  c += "{}".format(p)
  #  c += ", "
  #c += "]"
  #print(c)

  print("[{}]".format(", ".join(["{}".format(p) for p in perms])))


if __name__ == '__main__':
  main()