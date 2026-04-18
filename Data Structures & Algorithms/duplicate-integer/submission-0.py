from builtins import set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for num in nums:
            if num not in set1:
                set1.add(num)
            elif num in set1:
                return True
        return False
        