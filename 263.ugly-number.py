#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            changed = False
            for p in [2, 3, 5]:
                if n % p == 0:
                    n = n // p
                    changed = True
            if not changed:
                return False
        return True
# @lc code=end

