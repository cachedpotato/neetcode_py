def rob(nums) -> int:
  #can either rob current house and not rob the next one,
  #or can skip current house and rob the one after

  #[rob1, rob2, curr, curr+1, curr+2....]
  #[.....[rob1, rob2, curr, ..........]]
  # -----#------subproblem-------------#
  rob1 = rob2 = 0
  for n in nums:
    temp = max(rob1 + n, rob2)
    #move 1 forward
    rob1 = rob2
    rob2 = temp
  
  return rob2

def main():
  nums = [2, 9, 8, 3, 6]
  print(rob(nums))

if __name__ == "__main__":
  main()