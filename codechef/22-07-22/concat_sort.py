def solve(n, arr):
    sorted_arr = sorted(arr)
    counter1 = 0
    counter2 = 0
    zeros = [0] * n
    for i in range(2):
        counter1 = 0
        while counter1 < n:
            if not zeros[counter1] and arr[counter1] == sorted_arr[counter2]:
                zeros[counter1] = 1
                counter1 += 1
                counter2 += 1
            else:
                counter1 += 1
    return "YES" if counter1 == counter2 else "NO"

for _ in range(int(input())):
    
    n = int(input())
    print(solve(int(input()), list(map(int, input().split()))))    