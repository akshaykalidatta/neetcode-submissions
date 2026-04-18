class Solution:
    def helper(self, i, currword):
        if len(currword) == len(self.digits):
            self.ans.append(currword)
            return 

        for j in self.mapping[self.digits[i]]:
            # currword += j
            self.helper(i+1, currword + j)
            # currowrd = currword[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        self.digits = digits
        self.ans = []
        self.mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        currword = ''
        self.helper(0, currword)
        return self.ans