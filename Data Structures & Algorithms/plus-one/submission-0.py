class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            digits[i] = digits[i] + carry
            carry = 0
            if digits[i] < 10:
                break
            else:
                digits[i] = digits[i] % 10
                carry = 1
            i-=1

        if carry == 1:
            return [1] + digits
        else:
            return digits