class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0]*(len(nums)+1) for _ in range(len(nums)+1)]

        for l in range(1, len(nums)-1):
            for i in range(1, len(nums)-l):
                j = i + l - 1
                ans = -1
                for k in range(i, j+1):
                    coins = nums[i-1]*nums[k]*nums[j+1]
                    ans = max(ans, coins + dp[i][k-1] + dp[k+1][j])
                dp[i][j] = ans

        return dp[1][len(nums)-2]
        