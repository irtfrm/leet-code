#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getTree(self, nums, left, right) -> TreeNode:
        if left > right:
            return None
        mid = -(-(left+right) // 2)
        root = TreeNode(nums[mid])
        root.left = self.getTree(nums, left, mid - 1)
        root.right = self.getTree(nums, mid + 1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left = 0
        right = len(nums) - 1
        return self.getTree(nums, left, right)
# @lc code=end

