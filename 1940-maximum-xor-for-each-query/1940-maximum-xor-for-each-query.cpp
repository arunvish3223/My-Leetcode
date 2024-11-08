class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int m = 0;
        vector<int> res;
        int n = (1 << maximumBit) - 1;
        for (int i : nums) {
            m ^= i;
            res.push_back(m ^ n);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};