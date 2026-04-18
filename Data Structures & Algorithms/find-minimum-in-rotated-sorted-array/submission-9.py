class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low<= high:
            mid = (low+high)//2
            if nums[mid] >= nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high] and nums[mid] > nums[mid-1]:
                high = mid - 1
            else:
                return nums[mid]

        return nums[mid]