class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s=0
        e=len(arr)-1
        mid=(s+e)//2
        while s<e:
            if arr[mid]<arr[mid+1]:
                s=mid+1
            else:
                e=mid
            mid=s+(e-s)//2
        return s
        