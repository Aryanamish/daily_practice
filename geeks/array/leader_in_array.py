def leader(arr):
    leader = [arr[-1]]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > leader[-1]:
            leader.append(arr[i])
    leader.reverse()
    return leader


print(leader([7, 10, 4, 10, 6, 5, 2]))
