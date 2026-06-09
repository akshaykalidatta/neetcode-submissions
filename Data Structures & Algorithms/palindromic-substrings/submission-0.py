class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            L = R = i
            while L >=0 and R<=len(s)-1 and s[L] == s[R]:
                ans += 1
                L-=1
                R+=1

            L, R = i, i+1
            while L >=0 and R<=len(s)-1 and s[L] == s[R]:
                ans += 1
                L-=1
                R+=1

        return ans