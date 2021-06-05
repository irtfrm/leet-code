#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ""
        carry = 0
        length = max(len(a), len(b))
        for i in range(0, length):
            S = carry
            if len(a)-i-1 >= 0:
                S += 1 if a[len(a)-i-1]=="1" else 0
            if len(b)-i-1 >= 0:
                S += 1 if b[len(b)-i-1]=="1" else 0
            ans = str(S % 2) + ans
            carry = S // 2
        if carry > 0:
            ans = str(carry) + ans
        return ans
# @lc code=end

