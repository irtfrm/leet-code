#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        pointer = head
        n = 0
        while pointer != None:
            stack.append(pointer.val)
            pointer = pointer.next
            n += 1

        pointer = head
        for i in range(n//2):
            if pointer.val != stack.pop():
                return False
            pointer = pointer.next
        return True
# @lc code=end

