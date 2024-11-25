class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int left, right;
            if (i == 0) left = INT_MIN;
            else left = nums[i - 1];
            if (i == n - 1) right = INT_MIN;
            else right = nums[i + 1];
            if (nums[i] > left && nums[i] > right) return i;
        }
        return 0;
    }
};