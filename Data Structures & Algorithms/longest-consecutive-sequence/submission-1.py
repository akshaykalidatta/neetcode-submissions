class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set1 = set()
        for i in nums:
            set1.add(i)

        starts = []
        ans = 1
        temp = 1

        for i in range(len(nums)):
            if (nums[i] - 1) not in set1:
                starts.append(nums[i])

        for start in starts:
            while (start+1) in set1:
                temp +=1
                start +=1
            else:
                ans = max(ans, temp)
                temp = 1
                continue

        return ans


        # while ans <= len(nums):
        #     if (minNum+1) in set1:
        #         temp +=1
        #         minNum += 1

        #     else:
        #         ans = max(temp, ans)
        #         minNum +=1

        return ans