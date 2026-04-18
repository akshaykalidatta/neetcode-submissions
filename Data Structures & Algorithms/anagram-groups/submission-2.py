class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            keys = [0] * 26
            for j in i:
                keys[ord(j)-ord('a')] += 1
            keys = tuple(keys)
            if keys in ans:
                ans[keys].append(i)
            else:
                ans[keys] = [i]
        fin = []
        for i in ans:
            fin.append(ans[i])

        return fin
