# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         dp = [nums[-2], nums[-1], 0]
#         i = len(nums)-3

#         while i >= 0:
#             tmp = dp[0]
#             dp[0] = max(nums[i]+dp[1], dp[0])
#             dp[1] = tmp
#             i-=1

#         return dp[0]

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        dp[-1] = 0
        dp[-2] = nums[-1]
        i = len(nums)-2

        while i >= 0:
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])
            i-=1

        return dp[0]


        