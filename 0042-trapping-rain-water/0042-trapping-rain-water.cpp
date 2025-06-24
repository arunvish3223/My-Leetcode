class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> lge(n), rge(n);
        lge[0] = height[0];
        for(int i = 1; i < n; i++) {
            lge[i] = max(lge[i - 1], height[i]);
        }

        rge[n - 1] = height[n - 1];
        for(int i = n - 2; i >= 0; i--) {
            rge[i] = max(rge[i + 1], height[i]);
        }

        for(int i = 0; i < n; i++){
            lge[i]=min(lge[i],rge[i])-height[i];
        }
        return accumulate(lge.begin(), lge.end(), 0);
    }
};