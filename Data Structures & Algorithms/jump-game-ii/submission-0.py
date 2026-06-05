class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end = 0
        farthest = 0
        ans = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                ans += 1
                curr_end = farthest

        return ans 