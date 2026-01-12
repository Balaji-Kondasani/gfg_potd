'''
Time Complexity -- O(n)
Space Complexity -- O(1)

Technique Used -- Monotonic Deque 
'''

from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        
        dq=deque()
        
        i,j=0,0
        result=[]
        
        for j in range(len(arr)):
            
            while dq and dq[0]<=j-k:
                dq.popleft()
            while dq and arr[dq[-1]]<=arr[j]:
                dq.pop()
            dq.append(j)
            if j>=k-1:
                result.append(arr[dq[0]])
        return result