#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            s = str(i)
            if i % 15 == 0:
                s = "FizzBuzz"
            elif i % 3 == 0:
                s = "Fizz"
            elif i % 5 == 0:
                s = "Buzz"
            ans.append(s)
        return ans

# @lc code=end

