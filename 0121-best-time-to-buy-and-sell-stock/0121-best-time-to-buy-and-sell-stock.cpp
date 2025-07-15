class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        int lsfi=prices[0];
        int res=0;
        for(int i=1;i<n;i++){
            if(prices[i]<lsfi){
                lsfi=prices[i];
            }
            res=max(prices[i]-lsfi,res);
        }
        return res;
    }
};