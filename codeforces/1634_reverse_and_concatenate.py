def palindrone(s):
    if list(s) == list(reversed(s)):
        return True
    else:
        return False


for _ in range(int(input(""))):
    n, k = list(map(int, input("").split(" ")))
    s = input("")
    if k == 0:
        print(1)
    elif palindrone(s):
        print(1)
    else:
        print(2)
