class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        start=[]
        equal=[]
        end=[]
        for i in nums:
            if i<pivot:
                start.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                end.append(i)
        return start+equal+end


