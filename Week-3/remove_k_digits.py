'''
Approach 1
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Monotonic Decreasing Stack
'''

class Solution:
    def removeKdig(self, s, k):
        stack=[]
        if k==len(s):
            return 0
        for i in s:
            while stack and int(i)<int(stack[-1]) and k!=0:
                stack.pop()
                k-=1
            stack.append(i)
            if stack[0]=='0':
                del stack[0]
        if k:
            while stack and k!=0:
                k-=1
                stack.pop()
                
        
        if len(stack)==0:
            return 0
        return "".join(stack)