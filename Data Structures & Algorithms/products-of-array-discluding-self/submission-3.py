class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [0]* len(nums), [0]* len(nums)
        pre[0], suf[len(nums) - 1] = 1, 1
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1]*nums[i+1]

        ans = []
        for i in range(len(pre)):
            ans.append(pre[i]*suf[i])

        return ans