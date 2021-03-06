#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        next = 0
        if num < 10:
            return num
        while num > 0:
            next += num % 10
            num //= 10
        return self.addDigits(next)
# @lc code=end

