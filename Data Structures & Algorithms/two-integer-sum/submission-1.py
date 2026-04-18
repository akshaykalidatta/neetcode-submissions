class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st1 = {}
        ans = []
        for i in range(0, len(nums)):
            if (target - nums[i]) in st1:
                ans.append(st1[(target - nums[i])])
                ans.append(i)
            else:
                st1[nums[i]] = i

        return ans
