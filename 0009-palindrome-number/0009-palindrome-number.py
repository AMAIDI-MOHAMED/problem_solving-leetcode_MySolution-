class Solution(object):
    def isPalindrome(self, x):
        i=0
        x=str(x)
        if(int(x)<0):
            return False
        else:
            while(i<len(x)/2 ):
                if(x[i]!=x[len(x)-1-i]):
                    return False
                i=i+1
        return True

        