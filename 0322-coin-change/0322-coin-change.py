# Initialize a 1-D dp array with +inf values, set fp[0] as 0
# Iterate through each amount and each coin
# Set the dp[a] with the minumum of current dp[a] or 1 + dp[a-c] i.e for amount 7 with coins 1,3,4,5 dp[4] will be either the already computed dp[4] or 1 + dp[3]
# In the end return dp[amount] if it is different than previously set +inf value
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != 1e9 else -1