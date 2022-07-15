# cook your dish here

def solve(arr):
    was_one = True if arr[0] == 1 else False
    no_of_one = 0 if arr[0] == 0 else 1
    for i in range(1, len(arr)):
        if arr[i] == 0 and was_one is True:
            was_one = False
            continue
        elif arr[i] == 1 and was_one is False:
            no_of_one += 1
            was_one = True
    if no_of_one % 2 == 0 or no_of_one == 0:
        return "YES"
    return "NO"
    
# for _ in range():
    # arr = list(map(int, input().split()))
print(solve([0,0]))
    
            
    