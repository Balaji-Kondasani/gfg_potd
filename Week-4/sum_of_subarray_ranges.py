'''
Approach 1
Time Complexity -- O(n^2)
Space Complexity -- O(1)

Brute Force -- TLE Error
'''

class Solution:
    def subarrayRanges(self, arr):
        
        rangeSum=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                max_num=max(arr[i:j+1])
                min_num=min(arr[i:j+1])
                rangeSum+=(max_num-min_num)
        return rangeSum

'''
Approach 2
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Stack
'''

class Solution:
    
    def findNsl(self,arr):
        stack=[]
        result=[-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                idx=stack.pop()
                result[idx]=i
            stack.append(i)
        return result
    
    def findNsr(self,arr):
        stack=[]
        result=[len(arr)]*len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                idx=stack.pop()
                result[idx]=i
            stack.append(i)
        return result
                
    def findNgl(self,arr):
        stack=[]
        result=[-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                idx=stack.pop()
                result[idx]=i
            stack.append(i)
        return result
    
    def findNgr(self,arr):
        stack=[]
        result=[len(arr)]*len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<arr[i]:
                idx=stack.pop()
                result[idx]=i
            stack.append(i)
        return result
    
    def subarrayRanges(self, arr):
        
        NSL=self.findNsl(arr)
        NSR=self.findNsr(arr)
        
        NGL=self.findNgl(arr)
        NGR=self.findNgr(arr)
        
        subArrayMinimumSum=0
        subArrayMaximumSum=0
        
        for i in range(len(arr)):
            num=arr[i]*(i-NSL[i])*(NSR[i]-i)
            subArrayMinimumSum+=num
          
        for i in range(len(arr)):
            num=arr[i]*(i-NGL[i])*(NGR[i]-i)
            subArrayMaximumSum+=num    
        
        return subArrayMaximumSum - subArrayMinimumSum
            
            
