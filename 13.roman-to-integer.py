#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s):
            if ch == 'I':
                if i + 1 < len(s) and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    ans -= 1
                else:
                    ans += 1
            elif ch == 'V':
                ans += 5
            elif ch == 'X':
                if i + 1 < len(s) and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    ans -= 10
                else:
                    ans += 10
            elif ch == 'L':
                ans += 50
            elif ch == 'C':
                if i + 1 < len(s) and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    ans -= 100
                else:
                    ans += 100
            elif ch == 'D':
                ans += 500
            elif ch == 'M':
                ans += 1000
        return ans
# @lc code=end

