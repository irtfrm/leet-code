#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        l = list(s)
        while left < right:
            not_moved = True
            if not s[left] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                left += 1
                not_moved = False
            if not s[right] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                right -= 1
                not_moved = False

            if not_moved and left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        return "".join(l)

# @lc code=end

