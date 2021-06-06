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
        ans = x/2.0
        for i in range(30):
            if ans == 0:
                break
            ans = ans - (ans*ans-x)/(2*ans)
        return int(ans)
# @lc code=end

