class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ i
            ans = ans ^ nums[i]

        ans = ans ^ len(nums)

        return ans