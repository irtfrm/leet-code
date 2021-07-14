#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = []
        while len(self.stack) > 1:
            tmp.append(self.stack.pop())
        ans = self.stack.pop()
        while len(tmp) > 0:
            self.stack.append(tmp.pop())
        return ans

    def peek(self) -> int:
        """
        Get the front element.
        """
        tmp = []
        while len(self.stack) > 0:
            tmp.append(self.stack.pop())
        ans = tmp[-1]
        while len(tmp) > 0:
            self.stack.append(tmp.pop())
        return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

