class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lasts = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in lasts:
                lasts[s[i]] = i

        ans = []
        end = 0
        start = 0
        for i in range(len(s)):
            end = max(end, lasts[s[i]])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans