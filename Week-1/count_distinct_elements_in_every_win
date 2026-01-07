'''
Approach - 1
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Sliding Window
'''

class Solution:
    def countDistinct(self, arr, k):
        hashmap={}
        i,j=0,0
        result=[]
        
        while j<len(arr):
            if arr[j] in hashmap:
                hashmap[arr[j]]+=1
            else:
                hashmap[arr[j]]=1
            
            if j-i+1==k:
                result.append(len(hashmap.keys()))
                hashmap[arr[i]]-=1
                if hashmap[arr[i]]==0:
                    del hashmap[arr[i]]
                i+=1
            j+=1
        return result
            
        
        