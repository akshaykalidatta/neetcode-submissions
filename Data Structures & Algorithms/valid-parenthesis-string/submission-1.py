class Solution:
    def checkValidString(self, s: str) -> bool:
        s1, s2 = [], []
        for i in range(len(s)):
            if s[i] == '(':
                s1.append(i)
            if s[i] == '*':
                s2.append(i)
            if s[i] == ')':
                if s1:
                    s1.pop() 
                elif s2:
                    s2.pop()
                else:
                    return False           

        while s1 and s2:
            if s1[-1] > s2[-1]:
                return False
            s1.pop()
            s2.pop()

        return True if len(s1) == 0 else False
            