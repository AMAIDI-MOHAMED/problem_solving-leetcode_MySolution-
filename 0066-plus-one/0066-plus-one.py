class Solution(object):
    def plusOne(self, digits):
        res=[]
        ele=""
        for digit in digits:
            ele=ele+str(digit)
        ele=str(int(ele)+1)
        for el in ele:
            res.append(int(el))
        return res
        