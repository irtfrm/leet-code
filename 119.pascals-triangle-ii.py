#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
            if i == 0 or i == rowIndex:
                ans.append(1)
            else:
                ans.append(ans[i-1]*(rowIndex-i+1)//i)
        return ans
# @lc code=end

