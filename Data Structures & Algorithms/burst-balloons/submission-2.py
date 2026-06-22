class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[-1]*(len(nums)+1) for _ in range(len(nums)+1)]
        
        def rec(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]

            ans = -1
            for k in range(i, j+1):
                coins = nums[i-1]*nums[k]*nums[j+1]
                ans = max(ans, coins + rec(i,k-1) + rec(k+1,j))

            dp[i][j] = ans
            return ans

        return rec(1, len(nums)-2)