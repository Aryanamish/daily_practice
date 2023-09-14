from os import *
from sys import *
from collections import *
from math import *


def findPos(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return max(mid - 1, 0)
    return low


def divide(arr, count):
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    divide(L, count)
    divide(R, count)
    for i in range(len(L)-1, -1, -1):
        if L[i] > R[0]:
            count[0] += findPos(R, L[i])
        else:
            break
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def getInversions(arr, n):
    # Write your code here.
    count = [0]
    divide(arr, count)
    return count[0]


# Taking inpit using fast I/O.
def takeInput():
    n = 5
    arr = [2, 5, 1, 3, 4]
    return arr, n


# Main.
arr, n = takeInput()
print(getInversions(arr, n))
