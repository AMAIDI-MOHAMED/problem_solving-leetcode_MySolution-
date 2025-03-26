class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        output = [0] * n
        stack = []
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = i - idx
            stack.append(i)
        
        return output
