t = int(input())
for _ in range(t):
    n = int(input())
    x = input()
    one_found = False
    for i in x[:-2]:
        if i == '0':
            print('0', end="")
        elif i == '1' and one_found is False:
            print('1', end="")
            one_found = True
        else:
            print("0", end='')
    if one_found is False:
        print(x[-2:])
    else:
        print("00")
    print()
