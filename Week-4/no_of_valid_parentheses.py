'''
Approach 1 
Time Complexity -- O(n)
Space Complexity -- O(1)

Technique Used -- Standard Backtracking Template
'''

class Solution:
    def __init__(self):
        self.open=0
        self.close=0
        self.count=0
        self.nums=[]
    
    def solve(self,nums,n):
        if len(nums)==n:
            if self.open==self.close and  self.open+self.close==n:
                self.count+=1
            return 
        if self.open<n:
            nums.append('(')
            self.open+=1
            self.solve(nums,n)
            nums.pop()
            self.open-=1
        if self.close<self.open:
            nums.append(')')
            self.close+=1
            self.solve(nums,n)
            nums.pop()
            self.close-=1
        
    def findWays(self, n):
        
        self.solve(self.nums,n)
        return self.count
        
        