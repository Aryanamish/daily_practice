def solve(n,m):
    max_num = n
    for i in range(n, m):
        a = i
        b = m - (m%i)
        max_num = max(abs(a-b))

    return max_num

for _ in range(int(input())):
    solve(*list(map(int, input().split())))