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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        visited = set()
        for i in range(len(strs)):
            subans = []
            if strs[i] not in visited:
                subans.append(strs[i])
                visited.add(strs[i])
                for j in range(i+1,len(strs)):
                    if self.isAnagram(strs[i], strs[j]):
                        subans.append(strs[j])
                        visited.add(strs[j])
                ans.append(subans)

        return ans
            

        