class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        cur_min = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            else:
                ans = max(ans, prices[i] - cur_min)
        return ans