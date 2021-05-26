#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        push_dict = {"(": 0, "{": 1, "[": 2}
        pop_dict = {")": 0, "}": 1, "]": 2}
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(push_dict[c])
            elif len(stack)>0:
                poped = stack.pop()
                if pop_dict[c] != poped:
                    return False
            else:
                return False

        return len(stack) == 0
# @lc code=end

