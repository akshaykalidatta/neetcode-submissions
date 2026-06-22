class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1]*(len(p)+1) for _ in range(len(s)+1)]
        def rec(i, j):
            #base case
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            if dp[i][j]!=-1:
                return dp[i][j]

            ans = False
            if (i<=len(s)-1) and (s[i]==p[j] or p[j]=='.'):
                if j<len(p)-1 and p[j+1]=='*':
                    skip = rec(i, j+2)
                    take = rec(i+1, j)
                    ans = ans or skip or take
                else:
                    ans = ans or rec(i+1, j+1)
            else:
                if j<len(p)-1 and p[j+1]=='*':
                    skip = rec(i, j+2)
                    ans = ans or skip

            dp[i][j] = ans
            return dp[i][j]

        return rec(0, 0)