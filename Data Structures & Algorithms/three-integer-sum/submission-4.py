class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        if all(x==0 for x in nums):
            return [[0,0,0]]

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0-nums[i]
            while r>l:
                if nums[l]+nums[r]==target:
                    ans.append([nums[i],nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l]+nums[r]>target:
                    r -= 1
                elif nums[l]+nums[r]<target:
                    l += 1
                # l += 1
                # r -= 1

        set1 = set(tuple(an) for an in ans)
        ans = list(set1)
        
        return ans