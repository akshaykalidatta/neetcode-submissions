class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        first = nums[:len(nums)-1]
        last = nums[1:]

        dp1, dp2 = [first[-1], 0], [last[-1], 0]
        i, j = len(first)-2, len(last)-2

        while i>=0:
            tmp = dp1[0]
            dp1[0] = max(first[i]+dp1[1], dp1[0])
            dp1[1] = tmp
            i-=1

        while j>=0:
            tmp = dp2[0]
            dp2[0] = max(last[j]+dp2[1], dp2[0])
            dp2[1] = tmp
            j-=1

        return max(dp1[0], dp2[0])