class Solution:
    def search(self, liste: List[int], target: int) -> int:
        left,right=0,len(liste)-1
        while left<=right:
            midle=(left+right)//2
            if(target==liste[midle]):
                return midle
            elif(target<=liste[midle]):
                right=midle-1
            else:
                left=left+1
        return -1   