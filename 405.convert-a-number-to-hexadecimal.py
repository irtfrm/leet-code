#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
dct = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f"
}

class Solution:
    def toHex(self, num: int) -> str:
        ans = ""
        if num == 0:
            return "0"
        if num < 0:
            num += 4294967296
        while num != 0:
            ans = dct[num & 15] + ans
            num >>= 4
        return ans

# @lc code=end

