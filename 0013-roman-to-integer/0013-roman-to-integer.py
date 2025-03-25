class Solution:
    def romanToInt(self, s: str) -> int:
        HashMap={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sume=0
        for  i in range(len(s)-1):
            if(HashMap[s[i]]< HashMap[s[i+1]]):
                sume-=HashMap[s[i]]
            else:
                sume+=HashMap[s[i]]
        return sume+HashMap[s[-1]]
