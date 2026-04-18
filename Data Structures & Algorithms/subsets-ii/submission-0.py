class Solution:
    def helper(self, i, nums, currset, ans):
        if i >= len(nums):
            ans.append(currset.copy())
            return

        currset.append(nums[i])
        self.helper(i+1, nums, currset, ans)
        currset.pop()

        while i+1 < len(nums) and nums[i]== nums[i+1]:
            i += 1

        self.helper(i+1, nums, currset, ans)
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currset, ans = [], []
        self.helper(0, nums, currset, ans)
        return ans
        