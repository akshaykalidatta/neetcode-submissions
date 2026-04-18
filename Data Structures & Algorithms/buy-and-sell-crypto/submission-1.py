class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, ans = 0, 0
        for r in range(1, len(prices)):
            print(prices[l], prices[r])
            if prices[r] > prices[l]:
                ans = max(ans, (prices[r] - prices[l]))
            elif prices[r] <= prices[l]:
                l=r
            
        return ans