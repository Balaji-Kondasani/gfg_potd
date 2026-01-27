'''
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Nge To Right And Nge To Left
'''

class Solution:
    
    def findNgr(self,arr):
        result=[len(arr)]*len(arr)
        stack=[]
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<=arr[i]:
                index=stack.pop()
                result[index]=i
            stack.append(i)    
        return result
        
    def findNgl(self,arr):
        result=[-1]*len(arr)
        stack=[]
        
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                index=stack.pop()
                result[index]=i
            stack.append(i)
        return result    
            
    def maxPeople(self, arr):
        
        NGL=self.findNgl(arr)
        NGR=self.findNgr(arr)
        
        max_len=float("-inf")
        for i in range(len(arr)):
            max_len=max(max_len,(i-NGL[i])+(NGR[i]-1-i))
        
        return max_len
        