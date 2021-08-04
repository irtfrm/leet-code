#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 and 4294967296 % n == 0 and 0b1010101010101010101010101010101 & n == n:
            return True
        return False
# @lc code=end

