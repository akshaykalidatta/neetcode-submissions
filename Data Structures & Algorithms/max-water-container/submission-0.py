class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j, ans = 0, len(heights) - 1, 0

        while j>i:
            temp = min(heights[i], heights[j]) * (j-i)
            ans = max(temp, ans)
            if heights[i] > heights[j]:
                j-=1
            elif heights[j] >= heights[i]:
                i+=1

        return ans