#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class DoubleHash:
    def __init__(self) -> None:
        self.dct1 = {}
    def add(self, key1, key2, val):
        if not key1 in self.dct1:
            self.dct1[key1] = {}
        self.dct1[key1][key2] = val
    def contains(self, key1, key2):
        return key1 in self.dct1 and key2 in self.dct1[key1]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dct = {}
        ans = []
        for k, num in enumerate(nums):
            dct[-num] = k

        blacklist = DoubleHash()
        blacklist2 = DoubleHash()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sum = nums[i] + nums[j]
                if not blacklist.contains(i, j) and two_sum in dct and dct[two_sum] != i and dct[two_sum] != j:
                    if blacklist2.contains(min(nums[i], nums[j], -(two_sum)), max(nums[i], nums[j], -(two_sum))):
                        continue
                    ans.append([nums[i], nums[j], -(two_sum)])
                    k = dct[two_sum]
                    blacklist.add(min(i, k), max(i, k), None)
                    blacklist.add(min(j, k), max(j, k), None)
                    blacklist2.add(min(nums[i], nums[j], -(two_sum)), max(nums[i], nums[j], -(two_sum)), None)
        
        return ans

# @lc code=end

