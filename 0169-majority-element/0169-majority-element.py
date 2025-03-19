class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        maxim=len(nums)//2
        s=0 
        ele=nums[0]
        for i in range(1,len(nums)):
            if(s==maxim):
                return ele
            if(ele!=nums[i]):
                s=0
                ele=nums[i]
            else:
                s=s+1
        return ele