#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head: ListNode):
        node = head
        m = 0
        while node != None:
            node = node.next
            m += 1
        return m

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m = self.getLength(headA)
        n = self.getLength(headB)
        A = headA
        B = headB
        if m < n:
            A, B = B, A
            m, n = n, m
        for i in range(m - n):
            A = A.next
        while A != None:
            if A is B:
                return A
            A = A.next
            B = B.next
        return None


# @lc code=end

