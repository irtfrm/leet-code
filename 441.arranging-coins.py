#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(((1 + 8 * n) ** 0.5 - 1) / 2)
# @lc code=end

