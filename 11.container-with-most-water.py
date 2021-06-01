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
        height_sorted = [(i,height[i]) for i in range(len(height))]
        height_sorted = sorted(height_sorted, key=lambda x:x[1])

        left = 0
        right = len(height)-1
        for x in height_sorted:
            target_i = x[0]
            if target_i-left > right-target_i:
                M = max((target_i - left)*height[target_i], M)
            elif target_i-left < right-target_i:
                M = max((right - target_i)*height[target_i], M)
            while left < right and height[left] <= height[target_i]:
                left += 1
            while left < right and height[right] <= height[target_i]:
                right -= 1
        return M
# @lc code=end

