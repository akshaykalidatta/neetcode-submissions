class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        part = {}
        for i in s:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1

        ans = []
        length = 0
        rem = 0
        for i in s:
            if i not in part:
                part[i] = 1
                rem += 1
            else:
                part[i] += 1
            length += 1

            if part[i] == counts[i]:
                rem -= 1
            if rem==0:
                ans.append(length)
                part = {}
                length = 0
            
        return ans

