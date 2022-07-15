def solve(n,a,b):
    a_bin = list(bin(a)[2:])
    b_bin = list(bin(b)[2:])
    
    a_bin = ["0" for _ in range(len(b_bin) - len(a_bin))] + a_bin
    b_bin = ["0" for _ in range(len(a_bin) - len(b_bin))] + b_bin
    
    x = list()
    last_flipped = None
    
    for i in range(len(a_bin)):
        if a_bin[i] == b_bin[i]:
            x.append('0' if a_bin[i] == '1' else '1')
        elif last_flipped == 'a':
            x.append('0' if b_bin[i] == '1' else '0')
            last_flipped = 'b'
        else:
            x.append('0' if a_bin[i] == '1' else '0')
            last_flipped = 'a'
    if len(x) == 0:
        x[0] = '0'
    return int("".join(x), 2)

for _ in range(int(input())):
    print(solve(*list(map(int, input().split()))))