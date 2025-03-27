class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)-1):
            for j in range(len(arr)-1,-1,-1):
                if arr[i]*2==arr[j] and i!=j:
                    return True
                elif(arr[i]*2>arr[j] and i!=j):
                    break
        return False