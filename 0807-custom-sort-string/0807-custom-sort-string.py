from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        res = ''
        for i in order:
            if d[i] > 0:
                res += i * d[i]
                d[i] = 0
        for i in d:
            if d[i] > 0:
                res += i * d[i]
        return res
