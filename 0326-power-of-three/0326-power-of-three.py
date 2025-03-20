class Solution:
    def isPowerOfThree(self, x: int) -> bool:
        if x==0:
            return False
        div=0
        while(x!=1):
            div=x%3
            x=x//3
            if(div!=0):
                return False
        return True  