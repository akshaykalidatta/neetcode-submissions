import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        k = low + ((high - low)//2)
        ans = 0
        while low <= high:
            k = low + ((high - low)//2)
            temp = 0
            for i in range(len(piles)):
                temp += math.ceil(piles[i]/k)
            if temp > h:
                low = k + 1
            elif temp <= h:
                ans = k
                high = k - 1

        return ans


