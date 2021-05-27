#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        k = None
        if l1 != None and l2 != None:
            if l1.val <= l2.val:
                k = ListNode(l1.val)
                l1 = l1.next
            else:
                k = ListNode(l2.val)
                l2 = l2.next
        f = k
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                k_p = k
                k = ListNode(l1.val)
                k_p.next = k
                l1 = l1.next
            else:
                k_p = k
                k = ListNode(l2.val)
                k_p.next = k
                l2 = l2.next

        while l1 != None:
            k_p = k
            k = ListNode(l1.val)
            if k_p != None:
                k_p.next = k
            else:
                f = k
            l1 = l1.next

        while l2 != None:
            k_p = k
            k = ListNode(l2.val)
            if k_p != None:
                k_p.next = k
            else:
                f = k
            l2 = l2.next
        
        return f
# @lc code=end

