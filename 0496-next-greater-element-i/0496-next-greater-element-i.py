class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        v=[]
        for i in nums2[::-1]:
            if len(stack)==0 :
                v.append(-1)
            elif stack[-1] > i :
                v.append(stack[-1])
            else:
                while len(stack)>0 and stack[-1] <=i:
                    stack.pop()
                if len(stack)==0 :
                    v.append(-1)
                else:
                    v.append(stack[-1])
            stack.append(i)
        v.reverse()
        print(v)
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    res.append(v[j])
        return res