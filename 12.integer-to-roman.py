#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
dct = {0: "IV", 1: "XL", 2: "CD", 3: "M"}
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        for i in range(4):
            digit = num % 10
            num //= 10
            if digit == 0:
                continue
            if digit == 4:
                ans = dct[i] + ans
            elif digit == 9:
                ans = dct[i][0] + dct[i + 1][0] + ans
            elif digit >= 5:
                ans = dct[i][1] + dct[i][0] * (digit % 5) + ans
            else:
                ans = dct[i][0] * (digit % 5) + ans
        return ans

# @lc code=end

