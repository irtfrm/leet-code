#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length = len(s)
        dct = {}
        used = {}
        for i in range(length):
            if s[i] in dct:
                if dct[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                dct[s[i]] = t[i]
                used[t[i]] = None
        return True

# @lc code=end

