class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        ans = 0
        while i<j:
            area = (j-i)*(min(heights[j],heights[i]))
            ans = max(ans, area)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1

        return ans