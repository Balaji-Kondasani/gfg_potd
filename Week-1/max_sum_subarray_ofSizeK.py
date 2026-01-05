'''
Optimal Approach 
Time Complexity -- O(n)
Space Complexity -- O(n) 
'''
class Solution:
    def maxSubarraySum(self, arr, k):
        i,j=0,0
        max_len=float("-inf")
        curr=0
        while j<len(arr):
            curr+=arr[j]
            if j-i+1==k:
                max_len=max(curr,max_len)
                curr-=arr[i]
                i+=1
            j+=1
        return max_len
                
'''
we could have also solved the problem using double for loop or inner loop O(n^2) Complexity, 
but throws a TLE error on geeks for geeks 
'''
