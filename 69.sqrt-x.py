#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = x
        for i in range(30):
            ans = ans - (ans*ans-x)/(2*ans)
        return int(ans)
# @lc code=end

