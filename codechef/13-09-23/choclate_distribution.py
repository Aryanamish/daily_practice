# cook your dish here
def solve(n):
    if n & 1 == 0:
        return f"{1} {1} {n-2}"
    else:
        return f"{1} {n//2} {n//2}"


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
