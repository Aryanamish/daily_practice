# cook your dish here

def solve(n, arr):
    i, count =0,0
    while i< n:
        start = arr[i][0]
        end = arr[i][1]
        if start == end:
            count = max(count , 1)
            i += 1
            continue
        for j in range(i+1, n):
            if abs(i-j)+1 > abs(start -end) + 1:
                break
            if start >= arr[j][0] and end <=arr[j][1]:
                count = max(count, abs(i - j)+1)
            else:
                if start < arr[j][0]:

                    start  =max(start, arr[j][0])
                if end > arr[j][1]:
                    end = max(end, arr[j][1])
            
            if abs(start - end)+1 < count:

                break
        i += 1
    return count
                
# n = int(input())
arr = [
[2, 4],
[2, 4],
[1, 4],
[0, 7],
[0, 3],
[1, 2],
[1, 2],
[1, 1],

]
# for _ in range(n):
    # arr.append(list(map(int, input().split())))
print(solve(len(arr), arr))