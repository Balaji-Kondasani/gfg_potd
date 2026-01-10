'''
Approach 1
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Sliding Window with Hashmap 
'''

#Approach 1

class Solution:
    def countWays(self,s,k):
        hashmap={}
        i,j=0,0
        result,count=0,0
        
        while j<len(s):
            if s[j] in hashmap:
                hashmap[s[j]]+=1
            else:
                hashmap[s[j]]=1
            count=len(hashmap.keys())
            if count<=k:
                result+=(j-i+1)
            elif count>k:
                while count!=k:
                    hashmap[s[i]]-=1
                    if hashmap[s[i]]==0:
                        del hashmap[s[i]]
                    i+=1
                    count=len(hashmap.keys())
                if count<=k:
                    result+=(j-i+1)

            j+=1
        return result
    def countSubstr (self, s, k):
        at_most_k=self.countWays(s,k)
        at_most_k_minus1=self.countWays(s,k-1)
        return abs(at_most_k-at_most_k_minus1)