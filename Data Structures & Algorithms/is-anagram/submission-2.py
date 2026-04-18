class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dct = {}
        for i in s:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1

        for j in t:
            if j in dct:
                dct[j] -= 1
        if all(val == 0 for val in dct.values()):
            return True
        return False
        