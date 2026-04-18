class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        dct1, dct2 = {}, {}
        for s in s1:
            dct1[s] = dct1.get(s, 0) + 1

        l, r = 0, 0
        while r<len(s2):
            dct2[s2[r]] = dct2.get(s2[r], 0) + 1
            if (r-l+1) == len(s1):
                if dct1 == dct2:
                    return True
            if (r-l+1) > len(s1):
                dct2[s2[l]] -= 1 
                if dct2[s2[l]] == 0: del dct2[s2[l]]
                l+=1
                if dct1 == dct2:
                    return True
            r+=1

        return False
        