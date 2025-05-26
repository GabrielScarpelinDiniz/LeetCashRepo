class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxValue = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else: 
                if prices[right] - prices[left] > maxValue:
                    maxValue = prices[right] - prices[left]
            right += 1

        
        return maxValue