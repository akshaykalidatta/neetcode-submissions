class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = [0 for i in range(len(height))], [0 for i in range(len(height))]

        for i in range(len(height)-1):
            lmax[i+1] = max(lmax[i],height[i])

        for i in range(len(height)-1, 1, -1):
            rmax[i-1] = max(rmax[i],height[i])

        ans = 0
        for i in range(len(height)):
            if min(lmax[i],rmax[i]) > height[i]:
                ans += min(lmax[i],rmax[i]) - height[i]
        
        return ans