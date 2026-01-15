'''
Approach 1
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Greedy
'''

class Solution:
    def minCandy(self, arr):
        leftCandies=[1]*len(arr)
        rightCandies=[1]*len(arr)
        
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                leftCandies[i]=leftCandies[i-1]+1
        
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>arr[i+1]:
                rightCandies[i]=rightCandies[i+1]+1
                
        candies=0
        for i in range(len(arr)):
            candies+=(max(leftCandies[i],rightCandies[i]))
        return candies