#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = self.generate(numRows-1)
        last = ans[numRows-2]
        ls = []
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                ls.append(1)
            else:
                ls.append(last[i-1] + last[i])
        ans.append(ls)
        return ans
# @lc code=end

