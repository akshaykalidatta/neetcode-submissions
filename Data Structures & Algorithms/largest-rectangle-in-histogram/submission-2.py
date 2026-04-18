class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftmost = [-1]*len(heights)
        rightmost= [len(heights)]*len(heights)
        stack = []
        for i in range(len(heights)):
            while len(stack)!=0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack)!=0:
                leftmost[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(len(heights)-1, -1, -1):
            while len(stack)!=0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack)!=0:
                rightmost[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i in range(len(heights)):
            r = rightmost[i] - 1
            l = leftmost[i] + 1
            width = (r-l+1)
            ans = max(ans, heights[i]*width)

        return ans