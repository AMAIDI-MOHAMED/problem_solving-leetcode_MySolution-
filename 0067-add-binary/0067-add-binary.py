class Solution(object):
    def addBinary(self, a, b):
        while(len(a)!=len(b)):
            if(len(a)>len(b)):
                b="0"+b
            else:
                a="0"+a
        if(a==b and a=="0"):
            return "0"
        res=""
        carry=0
        for i in range(len(a)):
            if(a[len(a)-i-1]=='1' and b[len(a)-i-1]=='1' and carry==0):
                carry=1
                res='0'+res
            elif(a[len(a)-i-1]=='1' and b[len(a)-i-1]=='1' and carry==1):
                carry=1
                res='1'+res
            elif(carry==1 and ((a[len(a)-i-1]=='1' and b[len(a)-i-1]=='0') or (a[len(a)-i-1]=='1' and b[len(a)-i-1]=='0'))):
                carry=1
                res='0'+res
            elif(carry==0 and ((a[len(a)-i-1]=='1' and b[len(a)-i-1]=='0') or (a[len(a)-i-1]=='0' and b[len(a)-i-1]=='1'))):
                res='1'+res
            elif(a[len(a)-i-1]=='0' and b[len(a)-i-1]=='0' and carry==1):
                carry=0
                res='1'+res
            else:
                res='0'+res
        if(carry==1):
            res='1'+res
        return res