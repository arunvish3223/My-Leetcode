class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ums=sorted(nums)
        res=[]
        g=[]
        i=0
        j=len(nums)-1
        while(i<j):
            if ums[i]+ums[j]==target:
                res.append(ums[i])
                res.append(ums[j]) 
                break
            elif ums[i]+ums[j]<target:
                i+=1
            else:
                j-=1     
        for i in range(len(nums)):
            if res[0]==nums[i]:
                g.append(i)
        for i in range(len(nums)):
            if res[1]==nums[i]:
                g.append(i)
        return sorted(set(g))

        
