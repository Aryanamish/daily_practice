#User function Template for python3


#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    from collections import deque
    
    q1 = deque()
    q2 = deque()
    q2.append(root)
    que_q = q1
    pop_q = q2
    ans = []
    reverse = False
    while len(q1) > 0 or len(q2) > 0:
        while len(pop_q) > 0:
            node = pop_q.popleft()
            if node.left is not None:
                que_q.append(node.left)
            if node.right is not None:
                que_q.append(node.right)
            ans.append(node.data)
        
        pop_q, que_q = que_q, pop_q
        if reverse is True:
            pop_q.reverse()
        reverse = not reverse
        
        
    return ans




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3



#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
    
    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return self.__str__()



    
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
        result = findSpiral(root)
        for value in result:
            print(value,end = " ")
        print()
        
        

# } Driver Code Ends