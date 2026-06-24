class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        limit = 7 if sign>0 else 8
        ans = 0
        x = abs(x)
        while x > 0:
            digit = x%10
            if ans > ((1<<31)-1)//10:
                return 0
            if ans == ((1<<31)-1)//10 and digit>limit:
                return 0
            ans = ans*10 + digit
            x = x//10

        return ans*sign
