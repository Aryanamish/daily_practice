from typing import *


def oddLove(n: int, b: int, c: int, a: List[int]) -> int:
    i,j = -1,0
    found_odd = False
    found_even = False
    swapped = 0
    no_of_odd = 0
    no_of_evens_together = 0
    if a[-1] %2 == 0:
        no_of_evens_together+=1
    if a[0] % 2 == 0:
        no_of_evens_together += 1

    while i < n and j < n:
        if a[j] == 0 or a[j] %2 == 0:
            if found_odd is True:
                found_odd = False
                found_even = False
                rev = a[i:j]
                rev.reverse()
                a = a[:i] + rev + a[j:]
                no_of_evens_together += 1
                i += no_of_odd
                no_of_odd = 0
                swapped += 1 
                continue
            if found_even is False:
                found_even = True
            if i == -1:
                i = j
        elif a[j] % 2 == 1 and found_even is True:
            no_of_odd += 1
            found_odd = True
        
        j += 1
    return min((swapped*c) + b, no_of_evens_together*b) if i != -1 else 0

print(oddLove(15, 1, 5, [4, 4, 7, 4, 7, 7, 8, 6, 4, 10, 3, 9, 2, 2, 1]))


# def funDistance(arr, start, end):
#     ans = []
#     min_r = min(start, end)
#     max_r = max(start, end)
#     for i in arr:
#         if min_r < i < max_r:
#             ans.append(i)
#     return ans

# funDistance([29,38,12,48,39,55], 30,50)