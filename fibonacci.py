class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def dp(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = dp(n - 1) + dp(n - 2)
                return memo[n]

        return dp(n)
