class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n=bin(n)
        s=''
        for i in n[2:]:
            if i=='0':
                s+='1'
            else:
                s+='0'
        return int(s,2)
