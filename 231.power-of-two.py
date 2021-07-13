#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True

# @lc code=end

