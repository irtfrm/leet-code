#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def calcSquaresOfDigits(self, n: int) -> int:
        m = n
        ans = 0
        while m != 0:
            ans += (m % 10) ** 2
            m //= 10
        return ans

    def isHappy(self, n: int) -> bool:
        hash = {}
        while not n in hash:
            hash[n] = None
            n = self.calcSquaresOfDigits(n)
        return n == 1
# @lc code=end

