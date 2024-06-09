def two_sum(nums, target):
  num_map = {}
  for idx, num in enumerate(nums):
    complement = target - num
    if num_map.get(complement) != None:
      j = num_map.get(complement)
      if j > idx: return [idx, j]
      else: return [j, idx]
    
    else:
      num_map[num] = idx
  
  return []

def main():
  nums = [1, 6, 7]
  target = 13
  print("result: {}".format(two_sum(nums, target)))

if __name__ == "__main__":
  main()