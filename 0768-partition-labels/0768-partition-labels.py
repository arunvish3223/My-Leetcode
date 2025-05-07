class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = defaultdict()
        res=[]
        end=0
        size=0
        for i in range(len(s)):
            last_idx[s[i]]=i
        for i in range(len(s)):
            size+=1
            end=max(end,last_idx[s[i]])
            if i==end:
                res.append(size)
                size=0
        return res
        