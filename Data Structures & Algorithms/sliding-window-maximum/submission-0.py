class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        l, r = 0, 0
        maxnum = float('-inf')
        while r<len(nums):
            maxnum = max(maxnum, nums[r])
            if (r-l+1) > k:
                if maxnum == nums[l]:
                    maxnum = max(nums[l+1:r+1])  
                l+=1  
            if (r-l+1) == k:
                ans.append(maxnum)

            r+=1

        return ans