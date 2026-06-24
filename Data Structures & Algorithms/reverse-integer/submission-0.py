class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        ans = 0
        x = abs(x)
        while x > 0:
            ans = ans*10 + x%10
            x = x//10

        ans = ans*sign
        return ans if ans <= (1<<31)-1 and ans >= -(1<<31) else 0