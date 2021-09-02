#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local, host = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            s.add(local + '@' + host)
        return len(s)
# @lc code=end
