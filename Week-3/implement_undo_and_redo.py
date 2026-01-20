'''
Approach 1
Time Complexity -- O(n)
Space Complexity -- O(n)

Technique Used -- Stack
'''

class Solution:
    def __init__(self):
        self.stack=[]
        self.Undo=[]
        self.result=[]
    def append(self, x):
        self.stack.append(x)

    def undo(self):
        if self.stack:
            self.Undo.append(self.stack.pop())

    def redo(self):
        if self.Undo:
            self.stack.append(self.Undo.pop())

    def read(self):
        return "".join(self.stack)