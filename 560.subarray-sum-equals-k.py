#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {}
        sums = 0
        count = 0
        dct[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += dct.get(sums - k, 0)
            dct[sums] = dct.get(sums, 0) + 1
        
        return count

# @lc code=end

