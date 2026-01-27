'''
Time Complexity -- O(n)
Space Complexity -- O(n)
'''

class Solution:
    def josephus(self, n, k):
        
        
        result=[]
        for i in range(1,n+1):
            result.append((i,i))
        i=0
        while len(result)>1:
            i=(i+k-1)%len(result)
            result.pop(i)
        
        return result[0][0]