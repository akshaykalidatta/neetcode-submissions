class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)):
            # if nums[i] == 0:
            #     break

            if i>0 and nums[i]==nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            target = 0-nums[i]
            while r>l:
                if nums[l]+nums[r]==target:
                    ans.append([nums[i],nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l]+nums[r]>target:
                    r -= 1
                elif nums[l]+nums[r]<target:
                    l += 1
        
        return ans