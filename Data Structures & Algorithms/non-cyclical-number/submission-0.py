class Solution:
    def isHappy(self, n: int) -> bool:
        #set
        nums= set()
        #extract digits and add
        while True:
            num = 0
            while n:
                num += (n%10)**2
                n = n//10
            if num == 1:
                return True
            if num in nums:
                return False
            nums.add(num)
            n = num
