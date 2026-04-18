class Solution:
    def helper(self, nums, perm, ans, visited):
        if len(perm) == len(nums):
            ans.append(perm.copy())
            return

        for j in range(0, len(nums)):
            if visited[j] is False:
                perm.append(nums[j]) 
                visited[j] = True
                self.helper(nums, perm, ans, visited)
                perm.pop()
                visited[j] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, perm = [], []
        self.helper(nums, perm, ans, [False]*len(nums))
        return ans
        