# cook your dish here

n = int(input())
for _ in range(n):
    x = int(input())
    num = [i for i in input()]
    i = 0
    while i < len(num) - 2:
        temp = num[i] + num[i+1] + num[i+2]
        temp = int(temp)
        if temp > 100:
            num[i] = '1'
            num[i+1] = '0'
            num[i+2] = '0'
        i += 1
    if num[-1] == '1' and num[-2] == '1':
        num[-1] = '0'

    print("".join(num))
