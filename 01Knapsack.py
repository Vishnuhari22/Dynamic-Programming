class Solution:
    def solveKnapsack(self, weights: List[int], values: List[int], capacity: int) -> int:
        memo = {}
        
        def dp(i, c):
            # 1. Base Cases
            if i < 0:
                return 0
            if c == 0:
                return 0
            
            # 2. Check Memo
            if (i, c) in memo:
                return memo[(i, c)]
            
            # 3. Decision Tree
            # If item is too heavy, we MUST skip it
            if weights[i] > c:
                memo[(i, c)] = dp(i - 1, c)
            else:
                # Max of (Skip, Take)
                skip = dp(i - 1, c)
                take = values[i] + dp(i - 1, c - weights[i]) # <--- Fixed here!
                memo[(i, c)] = max(skip, take)
                
            return memo[(i, c)]

        return dp(len(weights) - 1, capacity)
