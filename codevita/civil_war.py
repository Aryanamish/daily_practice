def solve(nums):
    last_sum = 0
    first_sum = 0
    n = len(nums)

    i = 0
    j = n - 1
    team1 = 0
    team2 = 0

    while i <= j:
        while i <= j and (nums[i] > 0 or first_sum == 0) and first_sum >= 0:
            first_sum += nums[i]
            i += 1

        while i <= j and (nums[j] > 0 or last_sum == 0) and last_sum >= 0:
            last_sum += nums[j]
            j -= 1

        if first_sum > last_sum:
            team1 += first_sum
            first_sum = 0
        else:
            team1 += last_sum
            last_sum = 0

        team1, team2 = team2, team1

    team1 += first_sum + last_sum
    return abs(team1 - team2)


n = int(input())
arr = list(map(int, input().split()))

print(solve(arr), end="")
