/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        auto n = nums.size();
        unordered_map<int, int> hash;

        for (int i = 0; i < n; i++)
        {
            auto n_i = nums[i];
            if (auto itr = hash.find(n_i); itr != hash.end())
            {
                vector<int> ans{i, itr->second};
                return ans;
            }
            hash[target-n_i] = i;
        }
        vector<int> ans;
        return ans;
    }
};
// @lc code=end

