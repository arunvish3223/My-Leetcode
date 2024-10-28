class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        c=0
        gums=set(nums)
        n=len(nums)
        for i in range(n):
            mx=0
            y=nums[i]**2
            while True:
                if y in gums:
                    mx+=1
                    y=y**2
                else:
                    break
            c=max(c,mx)
        c+=1
        if c<2:
            return -1
        else:
            return c