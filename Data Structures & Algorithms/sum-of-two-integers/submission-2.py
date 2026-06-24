class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        MAX_INT = 0x7fffffff

        a &= MASK
        b &= MASK

        ans = 0
        carry = 0

        for pos in range(32):
            i = (a >> pos) & 1
            j = (b >> pos) & 1

            ans |= ((i ^ j ^ carry) << pos)

            carry = (i & j) | (i & carry) | (j & carry)

        if ans & (1 << 31):
            return ~(ans ^ MASK)
        return ans