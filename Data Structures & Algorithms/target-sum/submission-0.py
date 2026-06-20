class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def rec(i, sumofnum):
            #base case
            if i > len(nums)-1:
                if sumofnum == target:
                    return 1
                else:
                    return 0
            if (i, sumofnum) in dp:
                return dp[(i,sumofnum)]

            neg = rec(i+1,sumofnum-nums[i])
            pos = rec(i+1, sumofnum+nums[i])
            ans = neg+pos
            dp[(i, sumofnum)] = ans

            return ans

        return rec(0, 0)