class Solution:
    def helper(self, i, nums, currset: List[int], ans):
        if i == len(nums):
            ans.append(currset.copy())
            return
        
        currset.append(nums[i])
        self.helper(i+1, nums, currset, ans)
        currset.pop()

        self.helper(i+1, nums, currset, ans)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, currset = [], []
        self.helper(0, nums, currset, ans)
        return ans