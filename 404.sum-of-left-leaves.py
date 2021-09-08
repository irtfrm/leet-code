#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        lchild = root.left
        ans = 0
        if lchild != None:
            if lchild.left == None and lchild.right == None:
                ans += lchild.val
            else:
                ans += self.sumOfLeftLeaves(lchild)
        if root.right != None:
            ans += self.sumOfLeftLeaves(root.right)
        return ans
# @lc code=end

