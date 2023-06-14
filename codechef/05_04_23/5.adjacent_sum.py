# cook your dish here
def solve(arr, n):
    if n <= 2: return "NO"
    arr.sort()
    z = arr[-1] + arr[-2]
    new1 = []
    new2 = []
    low = 0
    high = n - 1
    while low < high:
        if arr[low] == arr[high]: return "NO"
        new1.append(arr[low])
        new1.append(arr[high])
        new2.append(arr[low])
        new2.append(arr[high])
        
        if new1[-1] + new1[-2] >= z: return "NO"
        if new2[-1] + new2[-2] >= z: return "NO"
        low += 1
        high -= 1
        
    return 'YES'
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))
    
    