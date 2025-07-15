class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        int lsfi=prices[0];
        int msfi=prices[n-1];
        vector<int> lsf(n, 0);
        vector<int> msf(n, 0);
        for(int i=1;i<n;i++){
            if(prices[i]<lsfi){
                lsfi=prices[i];
            }
            lsf[i]=max(prices[i]-lsfi,lsf[i-1]);
        }
        for(int i=n-2;i>=0;i--){
            if(prices[i]>msfi){
                msfi=prices[i];
            }
            msf[i]=max(msfi-prices[i],msf[i+1]);
        }
        int res=0;
        for(int i =0;i<n;i++){
            res=max(lsf[i]+msf[i],res);
        }
        return res;
        
    }
};