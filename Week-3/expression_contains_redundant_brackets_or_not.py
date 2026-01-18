'''
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Stack
'''
class Solution():
    def checkRedundancy(self, s):
        flag=False
        stack=[]
        for i in s:
            if i!=')':
                stack.append(i)
            else:
                while stack[-1]!='(':
                    if stack[-1]=='+' or stack[-1]=='-' or stack[-1]=='*' or  stack[-1]=='/':
                        flag=True
                    stack.pop()
                if flag:
                    stack.pop()
                    flag=False
                else:
                    return True
        return False
