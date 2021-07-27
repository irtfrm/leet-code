#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = (left + right) // 2

        while left < right:
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    break
                right = mid
            else:
                if isBadVersion(mid + 1):
                    mid = mid + 1
                    break
                left = mid
            mid = (left + right) // 2

        return mid
# @lc code=end

