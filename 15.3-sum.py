#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    curr_l = nums[l]
                    curr_r = nums[r]
                    while l < len(nums) and nums[l] == curr_l:
                        l += 1
                    while 0 <= r and nums[r] == curr_r:
                        r -= 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        return ans

# @lc code=end

