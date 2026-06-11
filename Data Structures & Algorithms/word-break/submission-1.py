class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def rec(i):
            if i >= len(s):
                return True
            if i in dp:
                return dp[i]

            dp[i] = False
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    ans = rec(i+len(word))
                    if ans:
                        dp[i] = True
                        break

            return dp[i]
            
        return rec(0)