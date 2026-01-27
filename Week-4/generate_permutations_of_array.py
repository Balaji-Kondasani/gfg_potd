'''

Time Complexity -- O(2^n)
Space Complexity -- O(n)

Technique Used -- Backtracking with extra space
'''

class Solution:
    def __init__(self):
        self.result=[]
    def compute(self,arr,nums,visited):
        if len(nums)==len(arr):
            self.result.append(nums[:])
            return
        for i in range(len(arr)):
            
            if visited[i]!=1:
                nums.append(arr[i])
                visited[i]=1
                self.compute(arr,nums,visited)
                nums.pop()
                visited[i]=0
        
    def permuteDist(self, arr):
        nums=[]
        visited=[0]*len(arr)
        self.compute(arr,nums,visited)
        
        return self.result


'''
Time Complexity -- O(2^n)
Space Complexity -- O(1)
'''

class Solution:
    def __init__(self):
        self.result=[]
    def compute(self,arr,index):
        if index==len(arr):
            self.result.append(arr[:])
            return
        for i in range(index,len(arr)):
            arr[i],arr[index]=arr[index],arr[i]
            self.compute(arr,index+1)
            arr[i],arr[index]=arr[index],arr[i]
            
        
    def permuteDist(self, arr):
        index=0
        self.compute(arr,index)
        
        return self.result