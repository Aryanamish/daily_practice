t = input()
t = int(t)

for i in range(t):
    line = input()
    # line = '6 2 4'
    line = line.split()
    # line = ['6', '2', '4']
    for j in range(3):
        line[j] = int(line[j])
    print(line)


# 2
# 6 2 4
# 5 7 3
