class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        zero = 0 if 0 not in nums else 1
        if nums.count(0) > 1:
            return [0]*len(nums)
        if zero == 0:
            product = 1
            for i in nums:
                product = product*i
            for i in nums:
                ans.append(product//i)

        if zero == 1:
            product = 1
            for i in nums:
                product = product*i if i !=0 else product
            for i in nums:
                if i != 0:
                    ans.append(0)
                else:
                    ans.append(product)

        return ans
        