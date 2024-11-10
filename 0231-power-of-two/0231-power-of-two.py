class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        else:
            n=bin(n)
            return n[2:].count("1") ==1
        