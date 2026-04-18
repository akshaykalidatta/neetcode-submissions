class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        dct1, dct2 = {}, {}
        for i in t:
            dct1[i] = dct1.get(i, 0) + 1

        l, r = 0, 0
        ans =None
        while r<len(s):
            dct2[s[r]] = dct2.get(s[r], 0) + 1
            print(f"r={r}, s[r]={s[r]}, dct2={dct2}")
            while all(dct2.get(k, 0) >= v for k, v in dct1.items()):
                print(f"l={l}, r={r}, window={s[l:r+1]}, ans={ans}")
                if ans is None or len(s[l:r+1]) < len(ans):
                    ans = s[l:r+1]
                dct2[s[l]] -= 1
                if dct2[s[l]] == 0: del dct2[s[l]]
                l+=1
            r+=1

        return ans if ans is not None else ""
