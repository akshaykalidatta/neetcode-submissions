class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = []
        map1 = {}

        for i in nums:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1

        frq = [[] for i in range(len(nums) + 1)]
        for i,v in map1.items():
            frq[v].append(i)
        ans = []
        for i in range(len(frq)-1, 0, -1):
            for x in frq[i]:
                ans.append(x)
            if len(ans) == k:
                return ans

