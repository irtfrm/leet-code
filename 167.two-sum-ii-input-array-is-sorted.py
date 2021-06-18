#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while True:
            sum = numbers[left] + numbers[right]
            if sum == target:
                break
            elif sum > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]
# @lc code=end

