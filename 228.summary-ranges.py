#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def getRangeStr(self, begin, end):
        if begin == end:
            return str(begin)
        else:
            return str(begin) + "->" + str(end)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        prev = nums[0]
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - prev != 1:
                ans.append(self.getRangeStr(ans.pop(), prev))
                ans.append(nums[i])
            prev = nums[i]
        ans.append(self.getRangeStr(ans.pop(), prev))
        return ans

# @lc code=end

