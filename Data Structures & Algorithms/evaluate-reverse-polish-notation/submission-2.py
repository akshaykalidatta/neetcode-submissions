class Solution:
    def is_num(self, i: str) -> bool:
        try:
            int(i)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        for i in tokens:
            print(num)
            if self.is_num(i):
                num.append(int(i))
            if i == '+' or i == '-' or i == '*' or i == '/':
                num2 = int(num.pop())
                num1 = int(num.pop())
                if i == '+':
                    num.append(num1+num2)
                if i == '-':
                    num.append(num1-num2)
                if i == '*':
                    num.append(num1*num2)
                if i == '/':
                    num.append(int(num1/num2))

        return num[-1]