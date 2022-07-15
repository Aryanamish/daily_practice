try:
    from run import read_input
    read = read_input()
    input = read.input
except ImportError:
   pass



def check_a(l, count, missing, middle=False):
    m = (l[0] + l[2])/2
    if m == l[1]:
        return count + 1, missing
    if middle is True and int(m) == m:
        missing.append(int(m))
        return count, missing 
    return count, missing

for i in range(int(input(""))):
    g = [[],[],[]]
    g[0] = list(map(int, input("").split(' ')))
    g[1] = list(map(int, input("").split(' ')))
    g[2] = list(map(int, input("").split(' ')))
    t = g[1][1]
    g[1][1] = 1.1
    g[1].append(t)
    count = 0
    missing = []
    count, missing = check_a(g[0], count, missing, False)
    count, missing = check_a(g[1], count, missing, True)
    count, missing = check_a(g[2], count, missing, False)
    
    count, missing = check_a([g[0][0], g[1][0], g[2][0]], count, missing, False)
    count, missing = check_a([g[0][1], g[1][1], g[2][1]], count, missing, True)
    count, missing = check_a([g[0][2], g[1][2], g[2][2]], count, missing, False)
    
    count, missing = check_a([g[0][0], g[1][1], g[2][2]], count, missing, True)
    count, missing = check_a([g[0][2], g[1][1], g[2][0]], count, missing, True)

    print(f'Case #{i+1}: {count + missing.count(max(missing, key = missing.count)) if len(missing) != 0 else 0 }')