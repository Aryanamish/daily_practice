'''
return a max difference of a[j] - ar[i] where j > i
'''


def max_diff(arr):
    smallest = arr[0]
    ans = arr[1] - arr[0]
    for i in range(2, len(arr)):
        ans = max(ans, arr[i] - smallest)
        smallest = min(smallest, arr[i])
    return ans


a = [[2, 3, 10, 6, 4, 8, 1], [7, 9, 5, 6, 3, 2], [10, 20, 30], [30, 10, 8, 2]]
for i in a:
    print(max_diff(i))