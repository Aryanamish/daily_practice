def buy_sell(arr):
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            profit += arr[i] - arr[i - 1]

    return profit


print(buy_sell([1, 5, 3, 8, 12]))
