#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = abs(nums[i]) - 1
            if nums[num] > 0:
                nums[num] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
# @lc code=end

