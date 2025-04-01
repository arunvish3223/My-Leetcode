class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s=1
        e=len(arr)-2
        mid=s+(e-s)//2
        while s<=e:
            mid=s+(e-s)//2
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]<arr[mid]:
                s=mid+1
            else:
                e=mid-1
        return -1
        