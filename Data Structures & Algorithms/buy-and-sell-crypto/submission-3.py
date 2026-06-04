class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_price = 0

        # for i in range(len(prices)):
        #     bp = prices[i]

        #     for j in range(i+1, len(prices)):
        #         sp = prices[j]
        #         max_price = max(max_price, (sp - bp))
            
        # return max_price
        
        # l = 0
        # r = 1
        # mp = 0

        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         mp = max(mp, prices[r] - prices[l])
        #     else:
        #         l = r    
        #     r += 1
        
        # return mp

        l, r = 0, 1
        max_price = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_price = max(profit, max_price)
            else:
                l = r
            r += 1
        return max_price