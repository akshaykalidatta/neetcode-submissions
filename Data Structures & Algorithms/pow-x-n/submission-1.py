class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1

        ans = 1
        div = 0
        if n < 1:
            n = abs(n)
            div = 1

        while n:
            if n%2==0:
                x = x*x
                n = n//2
            else:
                ans = ans*x
                n-=1

        if div:
            return 1/ans
        else:
            return ans