class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        m=0
        res=[]
        n=(2**maximumBit)-1
        for i in nums:
            m^=i
            k=m^(n)
            res.append(k)
        return res[::-1]

        