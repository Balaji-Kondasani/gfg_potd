'''
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Stack
'''

class Solution:
    def nextFreqGreater(self, arr):
        hashmap={}
        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        stack=[]
        result=[-1]*len(arr)
        for i in range(len(arr)):
            
            while stack and hashmap[arr[i]]>hashmap[arr[stack[-1]]]:
                index=stack.pop()
                result[index]=arr[i]
            
            stack.append(i)
        
        return result