def minCostClimbingStairs(cost) -> int:
  #[0, 1, ........,cost[n - 3], cost[n-2], cost[n - 1]]
  #from stair n-3 downwards:
  #min(cost[n-3] + cost[n-2], cost[n-3] + cost[n-1])
  #[0, 1, ........,min(cost... ), cost[n-2], cost[n - 1]]
  #[0, 1, .....cost[n-4], minCost[n-3], cost[n-2]]/ cost[n - 1]]
  #---===========--subproblem--==========--------#

  for i in range(len(cost) - 3, -1, -1):
    cost[i] += min(cost[i + 1], cost[i + 2])
  
  return min(cost[0], cost[1])

def main():
  cost = [1, 2, 1, 2, 1, 1, 1]
  print(minCostClimbingStairs(cost))

if __name__ == "__main__":
  main()