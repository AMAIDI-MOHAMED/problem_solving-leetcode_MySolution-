class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxm=max(candies)
        liste=[]
        for i in range(0,len(candies)):
            liste.append(candies[i]+extraCandies>=maxm)
        return liste