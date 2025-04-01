class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length=len(nums)
        ans=[0]*(length*2)
        i=0
        while i<length:
            ans[i]=nums[i]
            ans[i+length]=nums[i]
            i+=1
        return ans
