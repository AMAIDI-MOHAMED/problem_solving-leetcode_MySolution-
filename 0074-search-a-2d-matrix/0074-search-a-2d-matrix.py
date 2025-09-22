class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l=0
        r=len(matrix)-1
        while l<=r :
            mid=(l+r)//2
            if(matrix[mid][0]<=target<=matrix[mid][-1]):
                # Found the right row, now search within it
                left=0
                right=len(matrix[mid])-1
                while left<=right :
                    m=(left+right)//2
                    if(matrix[mid][m]==target):
                        return True
                    elif(matrix[mid][m]>target):
                        right=m-1
                    else:
                        left=m+1
                return False
            elif(matrix[mid][0]>target):
                r=mid-1
            else:
                l=mid+1
        return False