class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        i = 0
        while i<32:
            if (n & 1) == 1:
                ans+=1
            n = n >> 1
            i+=1

        return ans