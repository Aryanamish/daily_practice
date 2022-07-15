# cook your dish here

def solve(x):
    bigger = x
    smaller = 1
    while bigger >= smaller:
        if bigger == smaller:
            print(bigger, end=" ")
            break
        print(bigger, end=" ")
        bigger -= 1
        print(smaller, end=" ")
        smaller += 1
    print()
    
for _ in range(int(input(""))):
    solve(*list(map(int, input().split())))