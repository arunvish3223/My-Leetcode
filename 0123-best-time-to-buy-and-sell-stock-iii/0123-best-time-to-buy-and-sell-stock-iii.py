class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        lsf=[0]*n
        msf=[0]*n
        lsfi=prices[0]
        msfi=prices[n-1]
        for i in range(len(prices)):
            if prices[i]<lsfi:
                lsfi=prices[i]
            lsf[i]=max(prices[i]-lsfi,lsf[i-1])
        for i in range(n - 2, -1, -1):
            if prices[i] > msfi:
                msfi = prices[i]
            msf[i] = max(msfi - prices[i], msf[i + 1])
        res=0
        for i in range(n):
            res=max(res,lsf[i]+msf[i])
        return res
        
        