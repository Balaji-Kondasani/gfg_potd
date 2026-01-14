'''
Approach 1
Time Complexity -- O(n*k)
Space Complexity -- O(n)
TLE Error on GFG -- 1110/1210 Test Cases Passed
'''

class Solution:
    def catchThieves(self, arr, k):
        count=0
        j=0
        marked=[False]*len(arr)
        for i in range(len(arr)):
            if arr[i]=='P':
                if i-k<0:
                    j=0
                else:
                    j=i-k
                found=False
                
                while j>=0 and j<=i:
                    if j>=0 and arr[j]=='T' and not marked[j]:
                        count+=1
                        marked[j]=True
                        found=True
                        break
                    else:
                        j+=1
                if not found:
                    j=i+1
                    while j<=len(arr)-1 and j<=i+k:
                        if j<=len(arr)-1 and arr[j]=='T' and not marked[j]:
                        
                            marked[j]=True
                            count+=1
                            break
                        else:
                            j+=1
        return count
                
'''
Approach -2 
Time Complexity -- O(n)
Space Comlpexity -- O(n)
Technique Used -- Greedy + Two Pointer
'''

class Solution:
    def catchThieves(self, arr, k):
        police=[]
        thieves=[]
        count=0
        for i in range(len(arr)):
            if arr[i] =='P':
                police.append(i)
            else:
                thieves.append(i)
        
        i,j=0,0
        while i<len(police) and j<len(thieves):
            if abs(police[i]-thieves[j])<=k:
                count+=1
                i+=1
                j+=1
            elif police[i]>thieves[j]:
                j+=1
            else:
                i+=1
        return count
                
