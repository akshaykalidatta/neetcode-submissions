class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        ans = []

        for i in range(0, len(nums)):
            if (target - nums[i]) in dct:
                ans.append(dct[(target - nums[i])])
                ans.append(i)
            else:
                dct[nums[i]] = i
        return ans