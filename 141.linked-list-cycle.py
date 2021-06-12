#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dct = {}

        node = head
        while node != None:
            if id(node) in dct:
                return True
            dct[id(node)] = None
            node = node.next
        return False
# @lc code=end

