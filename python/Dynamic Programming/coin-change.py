# https://leetcode.com/problems/coin-change/submissions/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        dp = [float('inf')] * (amount+1)
        
        for i in range(1,amount+1):
            if i in coins:
                dp[i] = 1
                continue
                
            for coin in coins:
                if i - coin > 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
                    # print(i, dp[i])
                    
            # print(i, dp[i])
        
        # print(dp)
        
        return dp[amount] if dp[amount] != float('inf') else -1 