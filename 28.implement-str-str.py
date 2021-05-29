#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ans = -1
        length = len(needle)
        if length == 0:
            return 0
        for i in range(len(haystack)-length+1):
            cond = True
            for j in range(length):
                if haystack[i+j] != needle[j]:
                    cond = False
                    break
            if cond:
                ans = i
                break
        return ans



# @lc code=end

