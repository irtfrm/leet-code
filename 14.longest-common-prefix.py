#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        min_len = min([len(str) for str in strs])
        for i in range(min_len):
            if all([strs[0][i] == str[i] for str in strs]):
                ans += strs[0][i]
            else:
                break
        return ans
# @lc code=end

