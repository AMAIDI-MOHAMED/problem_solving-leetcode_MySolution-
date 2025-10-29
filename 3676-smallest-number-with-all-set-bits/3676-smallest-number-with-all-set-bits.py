class Solution:
    def smallestNumber(self, n: int) -> int:
        x=1
        i=0
        while n>x :
            i+=1
            x+=2**i
        return x


        