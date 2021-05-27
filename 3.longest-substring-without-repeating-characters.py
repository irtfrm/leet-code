#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        MAX = 0
        dictionary = dict()
        while i < len(s):
            if dictionary.get(s[i]) == None:
                dictionary[s[i]] = 1
                MAX = max(MAX, len(dictionary))
                i += 1
            else:
                del dictionary[s[j]]
                j += 1
        return MAX

# @lc code=end

