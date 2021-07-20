#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if root.left != None:
            res += map(lambda x:str(root.val)+ "->" + x, self.binaryTreePaths(root.left))
        if root.right != None:
            res += map(lambda x:str(root.val)+ "->" + x, self.binaryTreePaths(root.right))
        if root.left == None and root.right == None:
            res.append(str(root.val))
        return res
# @lc code=end

