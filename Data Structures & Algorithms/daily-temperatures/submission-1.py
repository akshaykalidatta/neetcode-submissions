class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            while len(stack)!=0 and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)

        return ans
            