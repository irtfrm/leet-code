#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}
        for i, num in enumerate(nums):
            if (not num in dct) or i - dct[num] > k:
                dct[num] = i
            else:
                return True
        return False
# @lc code=end

