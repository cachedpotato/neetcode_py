from typing import List
def coinChange(coins: List[int], amount: int) -> int:
  #while we can use the backtracking method, it's rather slow
  #have a dp cache of 0 all the way to amount
  #dp[i] will depend on current value and 1 + dp[i - c in coins]

  dp = [amount + 1] * (amount + 1) #max value won't exceed amount + 1
  dp[0] = 0

  for i in range(1, amount + 1, 1):
    for c in coins:
      if i - c >= 0:
        dp[i] = min(dp[i], dp[i - c] + 1)
  
  return dp[amount] if dp[amount] != amount + 1 else -1

def main():
  coins = [1, 2, 5]
  amount = 9
  print(coinChange(coins, amount))


if __name__ == "__main__":
  main()
