#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0
        for num in nums:
            if ans == num:
                count += 1
            elif count != 0:
                count -= 1
            else:
                ans = num
                count = 1
        return ans

    def majorityElement2(self, nums: List[int]) -> int:
        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1
        ans = None
        MAX = 0
        for num in dct:
            if dct[num] > MAX:
                MAX = dct[num]
                ans = num
        return ans
# @lc code=end

