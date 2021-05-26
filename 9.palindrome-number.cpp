/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
public:
    int get_upper_digit(int x) {
        if ((x>=0 && x<10) || (0>x && x>-10))
            return 1;
        return get_upper_digit(x/10) * 10;
    }
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        auto upper = get_upper_digit(x);
        auto lower = 10;

        while (upper > 1) {
            if (x / upper != x % lower)
                return false;
            x = (x % upper)/10;
            upper /= 100;
        }
        return true;
    }
};
// @lc code=end

