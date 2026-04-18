class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        l, r = 0, 0
        maxnum = float('-inf')
        dq = deque()
        while r<len(nums):
            # print(dq)
            #clear smaller than r elements
            while len(dq)>0 and nums[dq[-1]] < nums[r]:
                dq.pop()
            #append nums[r] 
            dq.append(r)
            #if window greater, shrink and remove front if smaller than l
            if (r-l+1) > k:
                l+=1
                if dq[0] < l:
                    dq.popleft()
            #if window size==k append ans
            if (r-l+1) == k:
                ans.append(nums[dq[0]])
            r+=1

        return ans