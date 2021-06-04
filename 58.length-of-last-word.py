#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        ans = 0
        for ch in s:
            if ch == " ":
                if l > 0:
                    ans = l
                l = 0
            else:
                l += 1
        if l > 0:
            ans = l
        return ans
# @lc code=end

