class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = 0
        e = n//2+1
        lv = 0
        while s <= e:
            mid = s + (e - s) // 2
            cn = (mid * (mid + 1)) // 2
            print(mid)
            print(cn)
            print("  ")
            if cn <= n:
                lv = mid
                s = mid + 1
            else:
                e = mid - 1
        return lv
