#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        dct = {}
        dct2 = {}
        if len(words) != len(pattern):
            return False
        for i, word in enumerate(words):
            if word in dct and dct[word] != pattern[i]:
                return False
            if not word in dct:
                if pattern[i] in dct2:
                    return False
                else:
                    dct[word] = pattern[i]
                    dct2[pattern[i]] = word
        return True
# @lc code=end

