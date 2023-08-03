# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        INF = sys.maxsize
        cp = 0 # current profit
        cmin = INF # current min

        for i in range(len(prices)):
            cmin = min(cmin, prices[i])
            cp = max(cp, prices[i] - cmin)
    
        return cp


# too slow greedy solution

# cp = 0 # current profit
# cmin = prices[0] # current min
# for i in range(len(prices)):
#     if prices[i] < cmin:
#         cmin = prices[i]
#     for j in range(len(prices)):
#         pf = prices[j] - cmin # calc profit
#         if pf > cp and j > i:
#             cp = pf
# return cp