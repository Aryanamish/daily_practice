def solve(arr, n):
    a = arr.copy()
    x = min(arr)
    arr_new = [i-x for i in arr]
    arr_sum = sum(arr_new) + arr_new[0]
    arr_len = len(arr) + 1
    x = int((arr[0] - arr_sum)/arr_len)
    return [i+x for i in arr_new]

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    # print(solve(arr, n))