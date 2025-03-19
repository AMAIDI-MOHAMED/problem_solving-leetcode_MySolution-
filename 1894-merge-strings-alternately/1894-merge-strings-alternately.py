class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        i=0;j=0
        while(len(word1)>i and len(word2)>j):
            if(len(word)%2==0):
                word+=word1[i]
                i=i+1
            else:
                word+=word2[j]
                j=j+1
        if(len(word1)>len(word2)):
            word+=word1[i:len(word1)]
        else:
            word+=word2[j:len(word2)]
        return word