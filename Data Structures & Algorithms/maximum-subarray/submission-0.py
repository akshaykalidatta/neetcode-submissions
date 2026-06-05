class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        ans = float('-inf')

        for i in nums:
            curr_max = max(i, i + curr_max)
            ans = max(ans, curr_max)

        return ans
        