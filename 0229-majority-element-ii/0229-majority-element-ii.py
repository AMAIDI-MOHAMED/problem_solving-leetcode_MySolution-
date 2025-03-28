class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length=len(nums)
        if length==1:
            return [nums[0]]
        nums2=set(nums)
        appear=(length//3)+1
        liste=[]
        for x in nums2:
            appears=0
            for j in range(length):
                if x==nums[j]:
                    appears=appears+1
                if appear==appears:
                    liste.append(x)
                    break
        return liste