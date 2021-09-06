#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        for c in s:
            i -= ord(c)
        for c in t:
            i += ord(c)
        return chr(i)
# @lc code=end

