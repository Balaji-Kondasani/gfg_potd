'''
Approach 1
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Sliding Window with Hashmap 
'''

#Approach 1

class Solution:
    def countSubarrays(self, nums, k):
        hashmap={0:1}
        odd_count,result=0,0
        result=0
        for i in range(len(nums)):
            if nums[i]%2!=0:
                odd_count+=1
            if odd_count-k in hashmap:
                result+=hashmap[odd_count-k]
            if odd_count in hashmap:
                hashmap[odd_count]+=1
            else:
                hashmap[odd_count]=1
        return result
                
        
        
        