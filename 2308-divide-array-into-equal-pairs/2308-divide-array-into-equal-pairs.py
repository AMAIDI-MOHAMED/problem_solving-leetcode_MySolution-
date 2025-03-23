class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairs=len(nums)//2
        nums.sort()
        s=0
        for i in range(0,len(nums),2):
            if(nums[i]==nums[i+1]):
                s+=1
        return s==pairs