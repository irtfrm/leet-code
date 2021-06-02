#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        M = 0

        left = 0
        right = len(height)-1
        while left < right:
            min_height = min(height[left], height[right])
            M = max((right - left)*min_height, M)
            while left < right and height[left] <= min_height:
                left += 1
            while left < right and height[right] <= min_height:
                right -= 1
        return M
# @lc code=end

