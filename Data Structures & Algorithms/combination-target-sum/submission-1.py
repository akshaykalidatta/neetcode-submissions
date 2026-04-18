class Solution:
    def helper(self, i, nums, target, currset, ans):
        if sum(currset) > target:
            return

        if sum(currset) == target:
            ans.append(currset.copy())
            return
            
        if i == len(nums):
            return

        for j in range(i, len(nums)):
            currset.append(nums[j])
            self.helper(j, nums, target, currset, ans)
            currset.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, currset = [], []
        self.helper(0, nums, target, currset, ans)
        return ans