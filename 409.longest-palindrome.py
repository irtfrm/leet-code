#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dct = {}
        for ch in s:
            dct[ch] = dct.get(ch, 0) + 1
        even = False
        for key in dct:
            even = even or (dct[key] & 1 == 1)
            dct[key] = dct[key] // 2 * 2
        return sum(dct.values()) + (1 if even else 0)
# @lc code=end

