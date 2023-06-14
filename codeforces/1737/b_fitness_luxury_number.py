def solve(start, end):
    count = 0
    current_sq_no = int(pow(start, 0.5))
    current_sq_val = current_sq_no ** 2
    next_sq_val = (current_sq_no + 1) ** 2
    while current_sq_val <= end:
        in_between = next_sq_val - current_sq_val - 1
        count += in_between // current_sq_no
        if current_sq_no == end:
            break
        current_sq_no += 1
        current_sq_val = current_sq_no ** 2
        next_sq_val = min((current_sq_no + 1) ** 2, end+1)

    return count

# for _ in range(int(input())):

    # print(solve(*list(map(int, input().split()))))
ans = {1:1}
for i in range(2, 10**9):
    if i % int(pow(i, 0.5)) == 0:
        ans[i] = ans[i-1] + 1
    else:
        ans[i] = ans[i-1]

print(ans)