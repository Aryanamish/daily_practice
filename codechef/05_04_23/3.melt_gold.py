# cook your dish here
def solve(sol):
    for melting, klin in sol:
        ans = 0
        
        for i in range(1, melting - klin):
            if melting <= klin: break
            klin += i
            ans = i
        print(ans)

inp = [
[3, 2],
[5, 3],
[10, 5],
[10, 1],
[10, 2],
[10, 3],
[10, 4],
[10, 5],
[10, 6],
[10, 7],
[10, 8],
[10, 9],
[10, 10],
]
solve(inp)