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
    def detectCycle(self, head: ListNode) -> ListNode:
        normal = head
        fast = head
        i = 0
        while fast != None and fast.next != None:
            if i > 0 and normal == fast:
                fast = head
                while normal != fast:
                    normal = normal.next
                    fast = fast.next
                return normal
            normal = normal.next
            fast = fast.next.next
            i += 1
        return None
# @lc code=end

