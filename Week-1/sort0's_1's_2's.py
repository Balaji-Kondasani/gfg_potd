'''
Approach - 1
Time Complexity - O(n)
Space Complexity - O(n)
'''

#Approach-1
class Solution:
    def sort012(self, arr):
        hashmap={}
        for i in arr:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        zero_freq=hashmap[0]
        one_freq=hashmap[1]
        two_freq=hashmap[2]
        return [0]*zero_freq+[1]*one_freq+[2]*two_freq

'''
Approach - 2
Time Complexity -- O(n)
Space Complexity -- O(1)
'''

#Approach-2
class Solution:
    def sort012(self, arr):
        i,j,m=0,0,len(arr)-1
        while j <= m:
            if arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
                i+=1
            elif arr[j]==1:
                j+=1
            else:
                arr[m],arr[j]=arr[j],arr[m]
                m-=1