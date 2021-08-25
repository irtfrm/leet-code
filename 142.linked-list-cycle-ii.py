#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findPre(self, head, target, maxTrav):
        if target == head:
            return None
        node = head
        i = 0
        while node.next != target:
            node = node.next
            i += 1
            if i >= 2 * maxTrav:
                return None
        return node

    def isInCycle(self, target, maxTrav):
        node = target.next
        i = 0
        while i < 2 * maxTrav:
            if node == target:
                return True
            node = node.next
            i += 1
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        normal = head
        fast = head
        i = 0
        while fast != None and fast.next != None:
            if i > 0 and normal == fast:
                while self.isInCycle(normal, i):
                    normal = self.findPre(head, normal, i)
                    if normal == None:
                        return head
                return normal.next
            normal = normal.next
            fast = fast.next.next
            i += 1
        return None
# @lc code=end

