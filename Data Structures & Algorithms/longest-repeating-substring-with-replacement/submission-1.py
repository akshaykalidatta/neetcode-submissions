class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        dct = {}
        ans= 0
        max_freq = 0
        while r<len(s):
            if s[r] not in dct:
                dct[s[r]] = 1
            else:
                dct[s[r]] += 1

            max_freq = max(max_freq, dct[s[r]])
            if ((r-l+1)-max_freq) <= k:
                ans=max(ans, (r-l+1))
            elif ((r-l+1)-max_freq) > k:
                dct[s[l]] -= 1
                l+=1
            r+=1

        return ans
