class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        dp = {}
        def rec(i):
            nonlocal ans
            res = 0
            if i <= 0:
                ans = max(ans, 1)
                return 1
            if i in dp:
                return dp[i]
            for j in range(0, i):
                if nums[i] > nums[j]:
                    res = max(res, rec(j))

            dp[i] = res + 1
            ans = max(res+1, ans)
            return dp[i]

        for i in range(len(nums)):
            rec(i)
        return ans