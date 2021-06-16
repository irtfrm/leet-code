#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = []

        while len(stack) != 0:
            node = stack.pop()
            if node != None:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return reversed(ans)

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        ans = []
        ans += self.postorderTraversal(root.left)
        ans += self.postorderTraversal(root.right)
        ans.append(root.val)
        return ans
# @lc code=end

