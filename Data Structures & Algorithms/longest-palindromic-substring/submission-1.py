class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        ansStr = 0
        for i in range(len(s)):
            length = 0
            L = R = i
            while L>=0 and R<=len(s)-1 and s[L]==s[R]:
                length = (R-L+1)
                if length > ans:
                    ans = length
                    ansStr = L
                L-=1
                R+=1

            length = 0
            L, R = i, i+1
            while L>=0 and R<=len(s)-1 and s[L]==s[R]:
                length = (R-L+1)
                if length > ans:
                    ans = length
                    ansStr = L
                L-=1
                R+=1

        return s[ansStr:ansStr+ans]