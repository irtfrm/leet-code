#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def ans(self, n, memo):
        if n==1:
            return 1
        if n==2:
            return 2
        if n in memo:
            return memo[n]
        memo[n] = self.ans(n-1, memo) + self.ans(n-2, memo)
        return memo[n]
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ans(n, {})
# @lc code=end