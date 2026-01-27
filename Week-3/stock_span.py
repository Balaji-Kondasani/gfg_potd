'''
Approach 1
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Stack
'''

class Solution:
    def calculateSpan(self, arr):
        result=[]
        for i in range(len(arr)):
            count=0
            for j in range(i+1):
                if arr[j]<=arr[i]:
                    count+=1
                else:
                    count=0
            
            result.append(count)
            
        return result


'''
Approach 2
Time Complexity -- O(n^2)
Space Complexity -- O(1)

Brute Force
'''

class Solution:
    def calculateSpan(self, arr):
        
        stack=[]
        result=[]
        for i in arr:
            span=1
            while stack and stack[-1][0]<=i:
                span+=(stack[-1][1])
                stack.pop()
            stack.append([i,span])
            result.append(span)
        
        return result