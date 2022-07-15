
def solve(n, no_of_element, mex, arr):
    elements_required = {i for i in range(mex)}
    no_of_mex = 0
    for i in range(n):
        if i+1 > no_of_element:
            break
        if arr[i] in elements_required:
            elements_required.remove(arr[i])
        elif arr[i] == mex:
            no_of_mex += 1
    
    if len(elements_required) == 0 and no_of_element <= n-no_of_mex:
        return "YES"
    else:
        return "NO"
        


# Driver code
for _ in range(int(input())):
    print(solve(*list(map(int, input().split())), list(map(int, input().split()))))