class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def rec(i):
            ans = 0
            if i in dp:
                return dp[i]
            if i == 0:
                return 1 if int(s[i])!=0 else 0
            if i == 1:
                if int(s[i])!=0:
                    ans += rec(i-1)
                if int(s[i-1])!=0 and int(s[i-1:i+1])<=26:
                    ans +=1

                dp[i] = ans
                return ans
                
            if int(s[i])!=0:
                ans += rec(i-1)
            if int(s[i-1])!=0 and int(s[i-1:i+1])<=26:
                ans += rec(i-2)

            dp[i] = ans
            return ans

        # if int(s[0])==0: return 0
        return rec(len(s)-1)