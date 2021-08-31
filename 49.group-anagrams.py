#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        strs_new = []
        for str in strs:
            str_new = "".join(sorted(list(str)))
            if not str_new in dct:
                dct[str_new] = []
            dct[str_new].append(str)
            strs_new.append(str_new)
        strs_new.sort()
        ans = []
        for i, str in enumerate(strs_new):
            if i > 0 and strs_new[i - 1] == str:
                continue
            ans.append(dct[str])
        return ans


# @lc code=end

