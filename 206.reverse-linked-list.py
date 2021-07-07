#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        stack = []
        while head != None:
            stack.append(head)
            head = head.next
        node = tail = stack.pop()
        while len(stack) > 0:
            node.next = stack.pop()
            node = node.next
        node.next = None
        return tail

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        ans = ans_head = self.reverseList(head.next)
        while ans.next != None:
            ans = ans.next
        ans.next = head
        head.next = None
        return ans_head
# @lc code=end

