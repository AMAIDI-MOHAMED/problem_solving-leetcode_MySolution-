class Solution:
    def reverseVowels(self, s: str) -> str:
        voyelle=[]
        nonV=[]
        for c in s:
            if(c.lower() in ['a', 'e', 'i', 'o','u']):
                voyelle.append(c)
                nonV.append('voy')
            else:
                nonV.append(c)
        if(len(voyelle)==0):
            return s
        voyelle.reverse()
        j=0
        s=""
        for i in range(len(nonV)):
            if(nonV[i]=='voy'):
                s+=voyelle[j]
                j+=1
            else:
                s+=nonV[i]
        return s