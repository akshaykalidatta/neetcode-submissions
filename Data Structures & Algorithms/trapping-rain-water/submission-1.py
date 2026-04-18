class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax=[0]*len(height), [0]*len(height)
        for i in range(1, len(height)):
            lmax[i] = max(lmax[i-1], height[i-1])

        for i in range(len(height)-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i+1])

        ans = 0
        for i in range(0, len(height)-1):
            if min(lmax[i],rmax[i])>height[i]:
                ans += min(lmax[i],rmax[i])-height[i]

        return ans