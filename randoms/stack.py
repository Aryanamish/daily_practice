# In the beginning, we have the stack S0 = {}.
# In the first step, we copy S0 and place number 1 on top, so S1 = {1}.
# In the second step, we copy S1 and place 2 on top of it, S2 = {1, 2}.
# In the third step we copy S2 and remove number 2 from it, S3 = {1}.
# In the fourth step we copy S2 and denote the copy with S4,
# then count the numbers appearing in the newly created stack S4 and stack S3, the only such number is number 1 so the solution is 1.
# In the fifth step we copy S4 and remove number 2 from it, S5 = {1}.

import traceback
class Stack:
    def __init__(self, value=None):
        self.val = []
        self.length = 0
        if value is not None:
            self.val += value
            self.length += 1
    
    def push(self,val):
        self.val.append(val)
        self.length += 1
        return self
    
    @property
    def pop(self):
        self.length -= 1
        return self.val.pop()
    
    @property
    def peek(self):
        return self.val[-1]
    
    @property
    def count(self):
        return self.length
    
    def copy(self):
        s = Stack()
        s.val = self.val.copy()
        s.length = self.length
        return s
    
    def __str__(self):
        return repr(self.val)

    def __repr__(self):
        return repr(self.val)

class Solution:
    
    '''
    	instruction = [
        	['a', 0],
            ['a', 1],
            ['b', 2],
            ['c', 2, 3],
            ['b', 4]
        ]
    '''
    def game(self, instructions):
        stacks = {
            0: Stack()
        }
        
        for i in range(len(instructions)):
            inst = instructions[i]
            inst[1] = int(inst[1])
            if inst[0] == 'a':
                stacks[i+1] = stacks[inst[1]].copy()
                stacks[i+1].push(i+1)
            elif inst[0] == 'b':
                stacks[i+1] = stacks[inst[1]].copy()
                print(stacks[i+1].pop)
            elif inst[0] == 'c':
                inst[2] = int(inst[2])
                stacks[i+1] = stacks[inst[1]].copy()
                total_length = set(stacks[i+1].val).intersection(stacks[inst[2]].val)
                print(len(total_length))

instructions = [
    ['a', '0'],
    ['a', '1'],
    ['b', '2'],
    ['c', '2', '3'],
    ['b', '4'],
]

s = Solution()
s.game(instructions)
                
                