def find_freq(arr):
    if len(arr) == 0:
        print()
        return
    count = 0
    for i in range(len(arr)):
        if count == 0:
            count += 1
        elif arr[i] == arr[i - 1]:
            count += 1
        else:
            print(arr[i - 1], count, end=", ")
            count = 1
    print(arr[-1], count)


q = [[10, 10, 10, 25, 30, 30], [10, 10, 10, 10], [10, 20, 30], [2], []]
for i in q:
    find_freq(i)
