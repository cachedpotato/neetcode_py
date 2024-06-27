def rob2(nums) -> int:
  #robber question but houses are CIRCULAR
  #either we include the first or last, not both

  def rob(subList) -> int:
    rob1 = rob2 = 0
    for n in subList:
      temp = max(rob1 + n, rob2)
      rob1 = rob2
      rob2 = temp
    return rob2
  
  return max(rob(nums[1:]), rob(nums[:-1]))

def main():
  nums = [3, 4, 3]
  print(rob2(nums))

if __name__ == "__main__":
  main()