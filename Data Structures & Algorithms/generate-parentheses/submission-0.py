class Solution:
    def helper(self, n, currstr, ans, openb, closeb):
        if len(currstr) == 2*n:
            temp = currstr
            ans.append(temp)
            return

        if openb < n:
            self.helper(n, currstr + '(', ans, openb + 1, closeb)

        if openb > closeb:
            self.helper(n, currstr + ')', ans, openb, closeb + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        ans, currstr = [], ''
        self.helper(n, currstr, ans, 0, 0)
        return ans