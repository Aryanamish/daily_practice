# cook your dish here

def maximum_x(x):
    y = 0
    y2 = 2**y
    max_x = 0
    ans = 1
    while True:
        cur_max = x ^ int(x/y2)
        if cur_max > max_x:
            ans = y
            max_x = cur_max
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
    