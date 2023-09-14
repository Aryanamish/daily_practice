t = int(input())
for _ in range(t):
    n = int(input())
    x = input()
    position = -1
    for i in range(n):
        if x[i] == '1':
            position = i
            break

    if position == -1 or position == (n - 1) or position == (n - 2):
        print(x)
    else:
        for i in range(position):
            print('0', end='')
        print('1', end='')
        for i in range(position + 1, n):
            print('0', end='')
        print()
