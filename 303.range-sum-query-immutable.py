#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = nums[i] + self.sums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - self.sums[left - 1] if left > 0 else self.sums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

