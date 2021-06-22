#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def charToNumber(self, char: str) -> int:
        return ord(char) - ord("A")
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        exp = 1
        for char in reversed(columnTitle):
            ans += (self.charToNumber(char)+1)*exp
            exp *= 26
        return ans
# @lc code=end

