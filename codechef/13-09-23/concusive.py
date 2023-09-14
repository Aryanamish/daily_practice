for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = [0] * n
    for i in range(1, n, 2):
        res[i] = arr.pop()
    for i in range(0, n, 2):
        res[i] = arr.pop()
    not_concussive = False
    for i in range(1, n - 1):
        if not ((res[i - 1] < res[i] > res[i + 1]) or (res[i - 1] > res[i] < res[i + 1])):
            not_concussive = True
    print(-1 if not_concussive else " ".join(map(str, res)))
