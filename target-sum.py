class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, t):
            if i < 0:
                return 1 if t == 0 else 0
            if (i, t) in memo:
                return memo[(i, t)]

            pos = dp(i - 1, t - nums[i])
            neg = dp(i - 1, t + nums[i])

            memo[(i, t)] = pos + neg
            return memo[(i, t)]
        
        return dp(len(nums) - 1, target)
