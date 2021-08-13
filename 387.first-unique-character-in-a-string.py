#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        for ch in s:
            if not ch in dct:
                dct[ch] = 1
            else:
                dct[ch] += 1
        for i, ch in enumerate(s):
            if dct[ch] == 1:
                return i
        return -1

# @lc code=end

