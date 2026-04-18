class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set1 = {}
        for i in s:
            if i not in set1:
                set1[i] = 1
            else:
                set1[i] += 1

        for j in t:
            if j in set1:
                set1[j] -= 1
        print(set1)
        for i in set1:
            if set1[i] != 0:
                return False
        return True