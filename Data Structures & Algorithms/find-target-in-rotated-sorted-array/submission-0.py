class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                #left half is sorted
                if nums[mid] > target >= nums[low]:
                    #Target lies in left sorted array
                    high = mid - 1
                else:
                    #Target lies in right unsorted array
                    low = mid + 1
            else:
                #right half is sorted
                if nums[mid] < target <= nums[high]:
                    #Target lies in right sorted array
                    low = mid + 1
                else:
                    #Target lies in left unsroted array
                    high = mid - 1

        return -1


                
