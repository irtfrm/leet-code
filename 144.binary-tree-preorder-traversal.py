#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            if node != None:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return ans

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        ans = []
        ans.append(root.val)
        ans += self.preorderTraversal(root.left)
        ans += self.preorderTraversal(root.right)
        return ans

# @lc code=end

