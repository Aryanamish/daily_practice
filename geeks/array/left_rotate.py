def rotate_by_one(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1
    return arr


def left_rotate(arr, x=0):

    def reverse(arr, low, high):
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    reverse(arr, 0, x - 1)
    reverse(arr, x, len(arr) - 1)
    arr.reverse()

    return arr


print(left_rotate([1, 2, 3, 4, 5, 6], 3))
