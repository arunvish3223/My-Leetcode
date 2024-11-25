class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                left = float('-inf')
            else:
                left = nums[i-1]
            if i == len(nums)-1 :
                right = float('-inf')
            else:
                right = nums[i+1]
            if left < nums[i] > right:
                return i
