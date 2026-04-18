class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        low = 0
        high = len(nums1) if len(nums1) < len(nums2) else len(nums2)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        while low<=high:
            i = (low+high)//2
            j = ((len(nums1) + len(nums2) + 1)//2) - i
            print(i, j)
            maxleft1 =nums1[i-1] if i>0 else float('-inf')
            maxleft2 = nums2[j-1] if j>0 else float('-inf')
            minright1 = nums1[i] if i<len(nums1) else float('inf')
            minright2 = nums2[j] if j<len(nums2) else float('inf')
            if maxleft1 <= minright2 and maxleft2 <= minright1:
                #ans found
                if (len(nums1)+len(nums2))%2 == 1:
                    return max(maxleft1, maxleft2)
                else:
                    return (max(maxleft1, maxleft2) + min(minright1, minright2))/2
            elif maxleft1 <= minright2 and maxleft2 > minright1:
                low = i+1

            elif maxleft1 > minright2 and maxleft2 <= minright1:
                high = i-1
            