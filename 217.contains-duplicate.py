#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for num in nums:
            if num in dct:
                return True
            else:
                dct[num] = None
        return False
# @lc code=end

