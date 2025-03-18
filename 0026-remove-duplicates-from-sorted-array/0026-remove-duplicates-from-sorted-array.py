class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        i = 1
        j = 0
        for i in range(1, k):
            if nums[i] != nums[i - 1]:
                nums[i - j] = nums[i]
            else:
                k=k-1
                j += 1
        return k