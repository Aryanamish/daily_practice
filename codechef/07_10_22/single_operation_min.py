# cook your dish here

def maximum_x(x):
    y = 1
    y2 = 2**y
    min_x = float('infinity')
    ans = 1
    while True:
        cur_min = x ^ int(x/y2)
        if cur_min < min_x:
            ans = y
            min_x = cur_min
        if int(x/y2) == 0:
            break
        y += 1
        y2 = y2*2
    return ans


for _ in range(int(input())):
    length = int(input())
    if length > 0:
        x = input()
        print(maximum_x(int(x, 2)))
    