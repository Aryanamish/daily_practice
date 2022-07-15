import random
def is_sorted(arr):
    prev = arr[0]
    
    for i in arr:
        if i < prev:
            return False
        else:
            prev = i
    return True
    
def flip(arr, i, j):
    b = arr[i:j+1]
    b.reverse()
    return arr[0:i] + b + arr[j+1:] 

def inc_j(i, j, n, let_i_catch_up):
    if let_i_catch_up:
        return [i+1, j]
    if j < n-1:
        return [i, j+1]
    else:
        return [i+1, j]

def solve2(n, s, arr):
    while True:
        element_swapped = 0
        i, j = 0, 1
        let_i_catch_up = False 

        while i<n and j < n:
            sub_arr = arr[i:j+1]
            sub_sum = sum(arr[i:j+1])
            if i + 1 == j:
                let_i_catch_up = False
            if sub_sum <= s:
                if arr[i] > arr[j] and i != j and i < j:
                    arr = flip(arr, i, j)
                    element_swapped += 1
                    i += 1
                else:
                    i, j = inc_j(i, j, n, let_i_catch_up)
            elif sub_sum > s:
                let_i_catch_up = True
                i += 1
                


        if is_sorted(arr):
            return True
        elif element_swapped == 0:
            return False


# for _ in range(1):
#     length = random.randint(1, 10**5)
#     s = random.randint(1, 2*10**9)
#     arr = [_ for _ in range(length)]
#     print(f"length is : {length}, sum is {s}")
#     print(solve(length, s, arr))

# for _ in range(int(input())):
    # print(solve(*list(map(int, input().split())), list(map(int, input().split()))))


q = [
    [4, 1, [1, 2, 3, 4], True],
    [4, 2, [2, 1, 3, 4], False],
    [5, 7, [3, 2, 2, 3, 3], True],
    [5, 3, [1, 1, 2, 2, 1], True],
    [5, 4, [1, 1, 1, 2, 1], True],
    [5, 4, [1, 1, 2, 1, 2], True],
]
for i in range(0, len(q)):
    ans = solve2(q[i][0], q[i][1], q[i][2])
    if ans == q[i][3]:
        pass
    else:
        print(f"failed for test case {i+1} {q[i][2]} Expected {q[i][3]} Got {ans}")