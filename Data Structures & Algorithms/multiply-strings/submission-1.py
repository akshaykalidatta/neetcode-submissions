class Solution:
    def add(self, num1: str, num2: str) -> str:
        carry  = 0
        ans=""
        i, j = len(num1)-1, len(num2)-1
        while i>=0 or j>=0 or carry:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            total = n1+n2+carry
            carry = total//10
            ans += str(total%10)
            i-=1
            j-=1

        return ans[::-1]


    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0": return "0"
        carry = 0
        ans = ""
        for i in range(len(num2)-1, -1, -1):
            tmp = ""
            n2 = int(num2[i])
            for j in range(len(num1)-1, -1, -1):
                n1 = int(num1[j])
                prd = n1*n2 + carry
                carry = 0
                if prd>9:
                    carry = prd//10
                    prd = prd%10
                tmp += str(prd)
            if carry:
                tmp += str(carry)
                carry = 0
            tmp = tmp[::-1] + "0"*(len(num2)-i-1)
            ans = self.add(ans, tmp)

        return ans

