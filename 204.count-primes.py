#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.hash = {}
    def isPrime(self, n: int) -> bool:
        i = 2
        ans = True
        while i**2 <= n:
            ans &= n % i != 0
            i += 1
        return ans

    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        if n == 3 or n == 4:
            return n-2
        if n in self.hash:
            return self.hash[n]
        if n % 2 == 0:
            ans = self.countPrimes(n - 2)
            if self.isPrime(n-1):
                ans += 1
            self.hash[n] = ans
        else:
            ans = self.countPrimes(n - 1)
        return ans
# @lc code=end

