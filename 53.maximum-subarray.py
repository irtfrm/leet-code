#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = nums[0]
        ans = S
        for i in range(1, len(nums)):
            S = max(S+nums[i], nums[i])
            ans = max(ans, S)
        return ans
# @lc code=end

