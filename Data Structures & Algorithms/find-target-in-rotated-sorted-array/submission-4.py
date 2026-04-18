class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low<= high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high] and  nums[mid] > nums[mid-1]:
                high = mid - 1
            else:
                pivot = mid
                break

        pivot = mid
        print(pivot)
        #left
        l1, r1 = 0, pivot-1
        print('l', l1, r1)
        while l1 <=r1:
            m1 = (l1+r1)//2
            if nums[m1] == target:
                return m1
            elif nums[m1] > target:
                r1=m1-1
            else:
                l1=m1+1

        #right  
        l2, r2 = pivot, len(nums)-1
        print('r', l2,r2)
        while l2 <=r2:
            m2 = (l2+r2)//2
            if nums[m2] == target:
                return m2
            elif nums[m2] > target:
                r2=m2-1
            else:
                l2=m2+1 

        return -1