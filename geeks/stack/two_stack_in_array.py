#User function Template for python3

#Function to push an integer into the stack1.


def push1(a, x):
    global top1
    global top2
    if top1 == top2:
        return -1
    a[top1 + 1] = x
    top1 += 1


#Function to push an integer into the stack2.
def push2(a, x):
    global top1
    global top2
    if top1 == top2:
        return -1
    a[top2 - 1] = x
    top2 -= 1


#Function to remove an element from top of the stack1.
def pop1(a):
    global top1
    global top2
    if top1 > -1:
        top1 -= 1
        return a[top1 + 1]
    else:
        return -1


#Function to remove an element from top of the stack2.
def pop2(a):
    global top1
    global top2
    if top2 < 101:
        top2 += 1
        return a[top2 - 1]
    else:
        return -1


#{
# Driver Code Starts
#Initial Template for Python 3

top2 = 101
top1 = -1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        a = [-1 for i in range(101)]  # array to be used for the 2 stacks.
        i = 0  # curr index
        while i < len(arr):
            if arr[i] == 1:
                if arr[i + 1] == 1:
                    push1(a, arr[i + 2])
                    i += 1
                else:
                    print(pop1(a), end=" ")
                i += 1
            else:
                if arr[i + 1] == 1:
                    push2(a, arr[i + 2])
                    i += 1
                else:
                    print(pop2(a), end=" ")
                i += 1
            i += 1
        top2 = 101
        top1 = -1
        print(' ')

# } Driver Code Ends