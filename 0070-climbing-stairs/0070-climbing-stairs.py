class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 2
        s=0
        step1=1
        step2=2
        for i in range(2,n):
            s=step1+step2
            step1=step2
            step2=s
        return s
