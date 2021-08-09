#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if i < len(nums1) and nums1[i] < nums2[j]:
                i += 1
            elif j < len(nums2) and nums1[i] > nums2[j]:
                j += 1
            elif i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                val = nums1[i]
                while i < len(nums1) and j < len(nums2) and nums1[i] == val and nums2[j] == val:
                    i += 1
                    j += 1
                    ans.append(val)
                while i < len(nums1) and nums1[i] == val:
                    i += 1
                while j < len(nums2) and nums2[j] == val:
                    j += 1
        return ans
# @lc code=end

