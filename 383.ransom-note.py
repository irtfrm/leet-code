#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct = {}
        for s in magazine:
            if not s in dct:
                dct[s] = 1
            else:
                dct[s] += 1
        for s in ransomNote:
            if not s in dct or dct[s] == 0:
                return False
            else:
                dct[s] -= 1
        return True
# @lc code=end

