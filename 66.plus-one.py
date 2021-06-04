#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        ans = []
        for digit in reversed(digits):
            tmp = (digit + carry) % 10
            carry = (digit + carry) // 10
            ans.append(tmp)
        if carry > 0:
            ans.append(carry)
        return reversed(ans)

# @lc code=end

