def solve(arr):
    i = 0
    j = 0
    while i < len(arr) and j < len(arr):
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i] != 0:
            i += 1
        if arr[j] == 0:
            j += 1
    return arr


print(solve([1, 0, 2, 5, 0, 0, 13, 0, 5]))
