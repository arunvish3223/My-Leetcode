import numpy as np
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while i < 32:
            if 2**i == n:
                return True
            i += 1
        return False
        