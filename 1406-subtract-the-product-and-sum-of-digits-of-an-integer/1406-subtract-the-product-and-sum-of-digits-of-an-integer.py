class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=n
        s,m=0,1
        while n>0:
            s+=n%10
            n=n//10
        while a>0:
            m*=a%10
            a=a//10
        return m-s