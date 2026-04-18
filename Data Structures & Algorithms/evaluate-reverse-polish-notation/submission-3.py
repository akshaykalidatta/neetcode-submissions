class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in tokens:
            if i not in '+' and i not in '-' and i not in '*' and i not in '/':
                print(i, "pushed")
                stack.append(i)
            else:
                print(i, "evaluating")
                b = int(stack.pop())
                a = int(stack.pop())
                if i =='+':
                    stack.append(a+b)
                if i =='-':
                    stack.append(a-b)
                if i =='*':
                    stack.append(a*b)
                if i =='/':
                    stack.append(a/b)
            print(stack)
        return int(stack.pop())