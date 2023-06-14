from os import *
from sys import *
from collections import *
from math import *

def findMedian(arr, n, m):

    start = 0
    last = m - 1
    ans = []
    while last < n:
        ans.append(get_median(arr, start, last, m))
        start += 1
        last += 1
    return ans

def get_median(arr, start, end, length):
    median = start + (length//2)
    ans = float(arr[median])
    if length % 2 == 0:
        ans += arr[median-1]
        ans /= 2
    return ans
    

print(findMedian([1, 2, 3, 4], 4,4))