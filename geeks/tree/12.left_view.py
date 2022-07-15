#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView_loop(root):
    
    from collections import deque
    
    q1 = deque()
    q1.append(root)
    q1.append(None)
    ans = []
    left_element = True
    while len(q1) > 0:
        node = q1.popleft()
        if node is None:
            left_element = True
            if len(q1) > 0:
                q1.append(None)
            continue
        elif q1[-1] is None:
            if node.left is not None:
                q1.append(node.left)
                
            elif node.right is not None:
                q1.append(node.right)
        
        if left_element:
            ans.append(node.data)
            left_element = not left_element
    return ans

def LeftView(root):
    
    from collections import deque
    ans = []
    def recursion(node, level=1, max_height=[0]):
        if node is None:
            return
        
        if (max_height[0] < level):
            ans.append(node.data)
            max_height[0] += 1
        
        recursion(node.left, level + 1, max_height)
        recursion(node.right, level + 1, max_height)
        
    recursion(root, 1, [0])
    return ans

#{ 
#  Driver Code Starts
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        result = LeftView(root)
        for value in result:
            print(value,end=" ")
        print()

# } Driver Code Ends