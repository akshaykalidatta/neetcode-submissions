class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i]!=s[j]:
                return False
            i += 1
            j -= 1
        return True

    def helper(self, i, currpart):
        if i == len(self.s):
            self.ans.append(currpart.copy())
            return

        for j in range(i, len(self.s)):
            substr = self.s[i:j+1]
            if self.isPalindrome(substr):
                currpart.append(substr)
                self.helper(j+1, currpart)
                currpart.pop()


    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.ans = []
        self.helper(0, [])
        return self.ans