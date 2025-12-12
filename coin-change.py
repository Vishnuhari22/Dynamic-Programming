class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i,a):
            if i < 0:
                return float("inf")
            if a == 0:
                return 0
            
            if (i,a) in memo:
                return memo[(i,a)]
            
            if coins[i] > a:
                memo[(i,a)] = dp(i-1, a)
                return memo[(i,a)]
            
            memo[(i,a)] = min(dp(i-1,a), 1 + dp(i, a-coins[i]))
            return memo[(i,a)]
        
        res = dp(len(coins) - 1, amount)
        return res if res != float("inf") else -1
