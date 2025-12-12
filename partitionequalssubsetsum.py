class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        memo = {}

        def dp(i, t):
            if i < 0:
                return False
            if t == 0:
                return True

            if (i,t) in memo:
                return memo[(i,t)]
            if nums[i] > t:
                memo[(i,t)] = dp(i-1, t)
                return memo[(i,t)]
            else:
                memo[(i,t)] = dp(i-1, t) or dp(i-1, t-nums[i])
                return memo[(i,t)]

        return dp(len(nums) - 1, target)
            
