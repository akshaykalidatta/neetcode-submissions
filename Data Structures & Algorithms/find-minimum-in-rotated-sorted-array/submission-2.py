class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            med = (high+low)//2
            if nums[med] >= nums[high]:
                low = med+1
            elif nums[med] < nums[high] and nums[med] >= nums[med-1]:
                high = med-1
            else:
                return nums[med]

        return nums[med]