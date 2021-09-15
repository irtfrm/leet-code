#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            s = carry
            if i >= 0:
                s += ord(num1[i]) - ord('0')
            if j >= 0:
                s += ord(num2[j]) - ord('0')
            carry = s // 10
            res = str(s % 10) + res
            i -= 1
            j -= 1
        if carry > 0:
            res = str(carry) + res
        return res
# @lc code=end

