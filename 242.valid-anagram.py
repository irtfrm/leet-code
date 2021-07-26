#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s = {}
        for ch in s:
            if not ch in dct_s:
                dct_s[ch] = 1
            else:
                dct_s[ch] += 1
        
        dct_t = {}
        for ch in t:
            if not ch in dct_t:
                dct_t[ch] = 1
            else:
                dct_t[ch] += 1
        
        for ch in dct_s:
            if not ch in dct_t:
                return False
            elif dct_s[ch] != dct_t[ch]:
                return False
        
        for ch in dct_t:
            if not ch in dct_s:
                return False
            elif dct_s[ch] != dct_t[ch]:
                return False
        return True

# @lc code=end

