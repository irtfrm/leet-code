#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = 1000000
        ans = 1000000
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                three_sum = nums[l] + nums[r] + nums[i]
                if three_sum == target:
                    return target
                elif min_diff > abs(target - three_sum):
                    ans = three_sum
                    min_diff = abs(target - three_sum)
                if three_sum > target:
                    r -= 1
                else:
                    l += 1
        return ans
# @lc code=end

