class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        count = 0

        def dp(i,a):
            if i < 0:
                return 0
            if a == 0:
                return 1

            if (i,a) in memo:
                return memo[(i,a)]
            
            if coins[i] > a:
                memo[(i,a)] = dp(i-1, a)
                return memo[(i,a)]
            
            memo[(i,a)] = dp(i-1,a) + dp(i,a-coins[i])
            return memo[(i,a)]

        return dp(len(coins) - 1, amount)
