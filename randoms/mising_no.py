def find_missing(arr):
    n = len(arr)
    x1 = x2 = 0
    for i in range(1, n+2):
        x1 = x1^i
        try:
            x2 = x2 ^ arr[i-1]
        except:
            pass
    return x1^x2

print(find_missing([1,2,4,5,6]))