class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        mod = 10**9 + 7
        dp[0]=1
        d={}
        for i in range(1,len(s)+1):
            dp[i] = (dp[i - 1] * 2) % mod
            if s[i - 1] in d:
                dp[i] = (dp[i] - dp[d[s[i - 1]] - 1]) % mod
            d[s[i - 1]] = i
        return (dp[len(s)]-1)% mod
                  