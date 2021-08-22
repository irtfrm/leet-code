#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            ans = ""
            div = 2 * numRows - 2
            for i in range(numRows):
                if i == 0 or i == numRows - 1:
                    ans += s[i::div]
                else:
                    j = i
                    k = div - i
                    while j < len(s) and k < len(s):
                        ans += s[j] + s[k]
                        j += div
                        k += div
                    if j < len(s):
                        ans += s[j]
            return ans
# @lc code=end

