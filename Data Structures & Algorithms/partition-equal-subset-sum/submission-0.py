class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2!=0: return False
        else: target = target//2

        dp = [False]*(target+1)
        dp[0] = True
        for i in nums:
            for j in range(len(dp)-1, i-1, -1):
                if dp[j-i]:
                    dp[j] = True

        print(dp)
        return dp[-1]
