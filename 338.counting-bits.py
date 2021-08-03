#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0] * (n + 1)
        ans[1] = 1
        power = -1
        for i in range(2, n + 1):
            if 131072 % i == 0:
                power += 1
            ans[i] = ans[i - (2 << power)] + 1
        return ans
# @lc code=end

