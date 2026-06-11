class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod, max_prod = nums[0], nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], nums[i]*max_prod, nums[i]*min_prod)
            min_prod = min(nums[i], nums[i]*max_prod, nums[i]*min_prod)
            max_prod = temp

            ans = max(ans, max(max_prod, min_prod))

        return ans