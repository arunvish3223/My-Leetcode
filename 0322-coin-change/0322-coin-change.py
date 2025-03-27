from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 0  
        
        for i in range(1, len(coins) + 1):  
            for j in range(1, amount + 1):  
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]  
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
        m=float('inf')
        for i in range(len(coins)+1):
            m=min(dp[i][amount],m)
        return -1 if m==float('inf') else m
