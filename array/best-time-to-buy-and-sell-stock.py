class Solution(object):
    #O(n) time O(1) Space complexity
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        difference = 0
        for i, num in enumerate(prices):
            if min_price > num:
                min_price = num
            if num - min_price > difference:
                difference = num - min_price
        return difference