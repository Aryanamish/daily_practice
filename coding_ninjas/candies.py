from typing import *


def peakArray(a: List[int]) -> List[int]:
    n = len(a)
    first_peek = True
    only_one_peek = False
    
    def check_peek(arr):
        no_of_peek = 0
        for i in range(len(arr)):
            if i == 0 and a[i] > a[i+1]:
                no_of_peek +=1
            elif i == (n-1) and a[i-1] < a[i]:
                no_of_peek += 1
            elif a[i-1] < a[i] > a[i+1]:
                no_of_peek += 1
        return no_of_peek == 1
    i = 0
    j = 0
    first_peek = True
    
    while True:
        if i==n:
            break
        if i == 0:
            if a[i] > a[i+1]:
                if first_peek is True:
                    first_peek = False
                    i+=1
                    continue
        elif(i==n-1):
            if a[i-1] < a[i]:
                #peek element
                if first_peek is True:
                    first_peek = False
                    i+=1
                    continue
                a[i-1], a[i] = a[i], a[i-1]
                i -= 2
        else:
            if a[i-1] < a[i] > a[i+1]:
                # peek element
                if first_peek is True:
                    first_peek = False
                    i+=1
                    continue
                
                a[i], a[i-1] = a[i-1], a[i]
        i+=1

    return a


print(peakArray([2, 4, 6, 8, 1, 5, 7]))