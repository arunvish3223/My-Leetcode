class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,m=0,1
        while n>0:
            s+=n%10
            m*=n%10
            n=n//10
        return m-s