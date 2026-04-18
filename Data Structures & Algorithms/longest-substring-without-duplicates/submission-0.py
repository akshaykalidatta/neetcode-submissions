class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        set1 = set()
        while r<len(s):
            while s[r] in set1:
                set1.remove(s[l])
                l+=1
            set1.add(s[r])
            ans = max(ans, (r-l+1))
            r+=1
            
        return ans