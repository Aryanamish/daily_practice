rank = int(input())
length = int(input())


arr = [i for i in range(1, length + 1)]

def solve(rank, arr):
    MOD = 26 - len(arr) + 1
    ptr = len(arr) - 1
    while rank >= MOD:
        rank = rank % MOD
        arr[ptr] += 1
        if arr[ptr] == 26:
            ptr -= 1

print(solve(rank, arr))


def generate(arr):
    for i in arr:
        
