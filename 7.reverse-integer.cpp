/*
 * @lc app=leetcode id=7 lang=cpp
 *
 * [7] Reverse Integer
 */

// @lc code=start
class Solution {
public:
    int get_digit(int x) {
        if ((x>=0 && x<10) || (0>x && x>-10))
        {
            return 1;
        }
        
        return get_digit(x/10) * 10;
    }
    int reverse(int x) {
        int max = 0x7FFFFFFF, min = -max-1;
        int num = x;
        int digit = get_digit(x);
        int ans = 0;
        while (num != 0)
        {
            if (num>0) {
                if ((num % 10)> 2 && digit==get_digit(max))
                    return 0;
                if (max - ans < (num % 10)*digit)
                    return 0;
            } else {
                if ((num % 10)< -2 && digit==get_digit(max))
                    return 0;
                if (min - ans > (num % 10)*digit)
                    return 0;
            }
            
            ans += (num % 10)*digit;
            num /= 10;
            digit /= 10;
        }
        
        return ans;
    }
};
// @lc code=end

