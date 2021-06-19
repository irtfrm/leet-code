#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def numToAlph(self, number):
        return chr(number + ord("A"))

    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber != 0:
            columnNumber -= 1
            ans = self.numToAlph((columnNumber) % 26) + ans
            columnNumber //= 26
        
        return ans


# @lc code=end

