for _ in range(int(input())):
    x, y, n, r = list(map(int, input().split())) 
    a,b,c,d = [0, 0, 0, 0]
    b = (r - (n * x))
    c = (y - x)
    a = b // c
    a = min(a, n)
    if a >= d:
        print(n - a, a)
    else:
        print(-1)