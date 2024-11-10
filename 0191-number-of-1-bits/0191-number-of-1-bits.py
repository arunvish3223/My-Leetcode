class Solution:
    def hammingWeight(self, n: int) -> int:
        x=bin(n)
        return x[2:].count("1")
        