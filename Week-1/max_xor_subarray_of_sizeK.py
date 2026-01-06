'''
Approach 1
Time Complexity -- O(n)
Space Complexity -- O(1)

Technique Used -- Two pointer
'''
class Solution:
    def maxSubarrayXOR(self, arr, k):
        i,j=0,0
        max_so_far=0
        curr=0
        while j<len(arr):
            curr^=arr[j]
            if j-i+1==k:
                max_so_far=max(max_so_far,curr)
                curr^=arr[i]
                i+=1
            j+=1
        return max_so_far
        
       
