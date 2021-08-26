#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        pre = None
        ans = head
        while node != None and node.next != None:
            if node.next.val == node.val:
                while node.next != None and node.next.val == node.val:
                    node = node.next
                if pre != None:
                    pre.next = node.next
                else:
                    ans = node.next
            else:
                pre = node
            node = node.next
        return ans
# @lc code=end

