# cook your dish here
def solve(n, s):
    last = None
    if len(s) == 1:
        return 0
    count = 0
    one_found = False
    for i in range(n-1, -1, -1):
        
        if s[i] == '0' and last is not None and one_found is True:
            s = s[:i+1] + s[last:i-1:-1] + s[last+1:]
            count += 1
            last = i+1
            one_found = False
        elif s[i] == '0' and last is None:
            last = i
        
        elif s[i] == '1' and last is not None:
            one_found = True
    if one_found is True:
        count += 1

    
    return count 
            
q = [
    [3, '000',0],
    [4, '1001', 1],
    [4, '1010', 2],
    [6, '010101', 2],
    [1, '1', 0],
    [2, '11', 0],
]
count =0
for i in q:
    count += 1
    ans = solve(i[0], list(i[1]))
    if ans == i[2]:
        pass
    else:
        print(f"Failed for test case {count} got '{ans}' expected '{i[2]}'")