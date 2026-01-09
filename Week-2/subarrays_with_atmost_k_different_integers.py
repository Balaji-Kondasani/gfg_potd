'''
Approach 1
Time Complexity -- O(n^2)
Space Complexity -- O(n)

Technique Used -- Check all subarrays and its distinct elements by making use of a set
Problem -- TLE error due to larger constraints
'''
class Solution:
    def countAtMostK(self, arr, k):
        
        count=0
    
        for i in range(len(arr)):
            unique=set()
            for j in range(i,len(arr)):
                if arr[j] in unique and len(unique)>=1 and len(unique)<=k:
                    count+=1
                    
                else:
                    unique.add(arr[j])
                    if len(unique)>=1 and len(unique)<=k:
                        count+=1
                        
        return count



'''
Approach 2
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Use hashmap to keep track of frequency of elements
'''

class Solution:
    def countAtMostK(self, arr, k):
        
        count=0
        hashmap={}
        i,result=0,0
        for j in range(len(arr)):
            if arr[j] in hashmap:
                hashmap[arr[j]]+=1
            else:
                hashmap[arr[j]]=1
            count=len(hashmap.keys())
            
            if count<=k:
                result+=(j-i+1)
            else:
                while count>k:
                    hashmap[arr[i]]-=1
                    if hashmap[arr[i]]==0:
                        del hashmap[arr[i]]
                    i+=1
                    count=len(hashmap.keys())
                result+=(j-i+1)
                        
        return result