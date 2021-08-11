#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            middle = (left + right) // 2
            g = guess(middle)
            if g > 0:
                left = middle + 1
            elif g < 0:
                right = middle - 1
            else:
                return middle
# @lc code=end

