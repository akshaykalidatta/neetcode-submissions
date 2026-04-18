class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        dct1, dct2 = {}, {}
        for i in t:
            dct1[i] = dct1.get(i, 0) + 1

        l, r = 0, 0
        ans =None
        have, need = 0, len(dct1)
        while r<len(s):
            dct2[s[r]] = dct2.get(s[r], 0) + 1
            if s[r] in dct1 and dct1[s[r]] == dct2[s[r]]:
                have +=1
            while have == need:
                if ans is None or (len(ans)>= len(s[l:r+1])):
                    ans = s[l:r+1]
                dct2[s[l]] -=1
                if s[l] in dct1 and dct2[s[l]] < dct1[s[l]]:
                    have -= 1
                l+=1
            r+=1

        return ans if ans is not None else ""
