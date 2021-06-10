#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = 0
        prices_min = prices[0]
        for i in range(1, len(prices)):
            dp = max(dp, prices[i] - prices_min)
            prices_min = min(prices_min, prices[i])

        return dp
# @lc code=end

