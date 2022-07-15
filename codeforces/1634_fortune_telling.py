def even(e):
    return True if e % 2 == 0 else False

def odd(e):
    return False if e % 2 == 0 else True

for _ in range(int(input())):
    n, x, y = list(map(int, input().split()))
    array = map(int, input().split())
    a_s = sum(array)
    if (odd(x) & odd(a_s) & even(y)) or (even(x) & odd(a_s) & odd(y)) or (even(x) & even(a_s) & even(y)) or (odd(x) & even(a_s) & odd(y)):
        print('Alice')
    else:
        print('Bob')
