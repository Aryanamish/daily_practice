def solve(arr):
    n = len(arr)
    stack = []

    h3 = float('-inf')

    for i in range(n - 1, -1, -1):

        while len(stack) > 0 and stack[-1] < arr[i]:
            h3 = stack.pop()

        stack.append(arr[i])

        if (arr[i] < h3):
            return True

    return False


print(solve([4, 7, 5, 6]))
print(solve([5, 4, 3, 2, 1]))
