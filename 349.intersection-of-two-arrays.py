#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
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
                ans.add(val)
                while i < len(nums1) and nums1[i] == val:
                    i += 1
                while j < len(nums2) and nums2[j] == val:
                    j += 1
        return list(ans)
# @lc code=end

