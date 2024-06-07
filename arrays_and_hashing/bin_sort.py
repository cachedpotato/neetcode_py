def top_k_freq(nums, k: int):
  #bin sort algorithm
  #bins are essentially list of lists
  #where the index number indicates the frequency
  #ex) bin[3] = [1, 2, 3]: 1, 2, 3 appears 3 times
  #for index to match the numbers, the total number of bins should be length of list + 1

  count = {}
  bins = [[] for i in range(len(nums) + 1)]

  #get count info
  for n in nums:
    count[n] = count.get(n, 0) + 1
  
  #update bin with the count hash map
  for n, c in count.items():
    bins[c].append(n)
  
  #return top k results
  #go DOWN the array
  out = []
  for i in range(len(nums) - 1, 0, -1):
    for n in bins[i]:
      out.append(n)
      if len(out) == k: return out

def main():
  nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5]
  k = 2
  print("top k frequent nums: {}".format(top_k_freq(nums, k)))

if __name__ == "__main__":
  main()