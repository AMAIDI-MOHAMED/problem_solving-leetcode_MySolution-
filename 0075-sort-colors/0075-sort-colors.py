class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r=nums.count(0)
        w=nums.count(1)
        length=len(nums)
        for i in range(length):
            if r!=0:
                nums[i]=0
                r-=1
            elif w!=0:
                nums[i]=1
                w-=1
            else:
                nums[i]=2

        