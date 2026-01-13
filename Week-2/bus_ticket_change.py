'''
Time Complexity -- O(n)
Space Complexity -- O(1)

Technique Used -- Greedy 
'''
class Solution:
    def canServe(self, arr):
        five_rupees=0
        ten_rupees=0
        for i in arr:
            if i==5:
                five_rupees+=1
            else:
                change=(i-5)//5
                if change==1 and five_rupees>0:
                    five_rupees-=1
                    ten_rupees+=1
                elif change==3 and five_rupees>=1 and ten_rupees>0:
                    five_rupees-=1
                    ten_rupees-=1
                elif change==3 and five_rupees>=3:
                    five_rupees-=3
                else:
                    return False
                    
        return True