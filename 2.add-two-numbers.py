#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def get_sum(self,l1,l2,carry):
        val = carry
        if l1 != None:
            val += l1.val
        if l2 != None:
            val += l2.val
        return val
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        k = None
        carry = 0
        while l1 != None or l2 != None:
            sum = self.get_sum(l1,l2,carry)
            new = ListNode(sum % 10)
            carry = sum // 10

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            if k != None:
                k.next = new
            else:
                ans = new
            k = new
        if carry != 0:
            new = ListNode(carry)
            k.next = new

        return ans
# @lc code=end

