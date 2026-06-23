class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            bit = 0
            while i > 0:
                if (i & 1) == 1:
                    bit += 1
                i = i >> 1
            
            ans.append(bit)

        return ans