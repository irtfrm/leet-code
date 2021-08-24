#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
dct = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        for i, digit in enumerate(digits):
            if i == 0:
                ans = dct[digit]
            else:
                ans_new = []
                for pre in ans:
                    for post in dct[digit]:
                        ans_new.append(pre + post)
                ans = ans_new
        return ans
# @lc code=end

