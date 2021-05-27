#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = None
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == t:
                nums.pop(i)
            else:
                i += 1
                t = num
        return len(nums)
# @lc code=end

