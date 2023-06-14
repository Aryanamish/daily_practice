t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    counts = {}
    arr.sort()
    for i in arr:
        c = counts.get(i, 0)
        c += 1
        counts[i] = c
    counts = [[key, counts[key]] for key in counts]
    counts.sort(key=lambda x: x[1], reverse = True)

    arr2 = []
    while len(counts) > 1:
        arr2.append(counts[-2][0])
        arr2.append(counts[-1][0])
        counts[-1][1] -= 1
        counts[-2][1] -= 1
        if counts[-2][1] == 0:
            x = counts.pop()
            counts.pop()
            counts.append(x)
        if counts[-1][1] == 0:
            counts.pop()
    if len(counts) > 0:
        if counts[-1][1] > 1:
            print(-1)
            continue
        else:
            arr2.append(counts[-1][0])
        counts.pop()
    for i in arr2:
        print(i, end=" ")
    print()
