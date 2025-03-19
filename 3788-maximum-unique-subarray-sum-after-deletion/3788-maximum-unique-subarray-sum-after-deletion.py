class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sets=set()
        sets.add(max(nums))
        s=max(nums)
        for num in nums:
            if (not(num in sets) and (num>0)):
                s+=num
                sets.add(num)
        return s