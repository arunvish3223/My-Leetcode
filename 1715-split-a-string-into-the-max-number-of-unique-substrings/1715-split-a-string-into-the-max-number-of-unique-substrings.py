class Solution:
    def all_possible_substrings(self, s, pos, ms, us):
        if pos==len(s):
            ms[0]=max(ms[0],len(us))
            return 
        tempstr=""
        for i in range(pos,len(s)):
            tempstr+=s[i]
            if tempstr not in us:
                us.add(tempstr)
                self.all_possible_substrings(s, i+1, ms, us)
                us.remove(tempstr)

    
    def maxUniqueSplit(self, s: str) -> int:
        ms =[0]
        us = set()
        self.all_possible_substrings(s, 0, ms, us)
        return ms[0]