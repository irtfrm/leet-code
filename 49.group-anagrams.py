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
        return dct.values()


# @lc code=end

