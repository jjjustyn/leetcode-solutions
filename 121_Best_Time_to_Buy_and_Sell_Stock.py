class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #finding the lowest valley followed by the highest peak (biggest difference)
        min_price = float('inf')
        max_profit = 0
        
        #iterate through prices array 
        for i in range(len(prices)):
            #if the current price is lower than the min price then update min_price
            if prices[i] < min_price:
                min_price = prices[i]
            #if the current profit is higher than max profit so far update max_profit
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
