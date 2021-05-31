#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        r = 0

        while True:
            if nums[(l+r)//2] == target:
                return (l+r)//2
            if l-r<2:
                break
            elif nums[(l+r)//2] > target:
                l = (l+r)//2
            else:
                r = (l+r)//2
        if (l+r)//2 == 0 and target < nums[0]:
            return 0
        return (l+r)//2+1
# @lc code=end

