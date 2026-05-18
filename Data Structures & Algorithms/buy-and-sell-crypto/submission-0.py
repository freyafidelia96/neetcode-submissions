class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i in range(len(prices)):
            bp = prices[i]

            for j in range(i+1, len(prices)):
                sp = prices[j]
                max_price = max(max_price, (sp - bp))
            
        return max_price
        