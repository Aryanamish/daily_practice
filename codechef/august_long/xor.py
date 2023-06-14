# cook your dish here
T = int(input())
for i in range(T):
    N,X,Y = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    i = 0
    while Y > 0:
        arr[i] = arr[i] ^ X
        
        
        if i+1 < len(arr) and arr[i] < arr[i+1]:
            i = i
        elif i+1 == len(arr):
            arr.sort()
            i=0
        else:
            i+=1
            
        Y-=1
    arr.sort()
    [print(i, end=" ") for i in arr]
    print()