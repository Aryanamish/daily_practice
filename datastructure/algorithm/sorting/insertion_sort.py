import parent
import random
from timer import performance

def rearrange(array, from_pos, to):
    return array[: to] + [array[from_pos]] + array[to: from_pos] + array[from_pos+1:]

@performance
def insertion_sort(array):
    length = len(array)
    for i in range(length):
        if array[i] < array[0]:
            array = rearrange(array, i, 0)
        else:
            for j in range(1, i):
                if array[j-1] <= array[i] and array[i] < array[j]:
                    array = rearrange(array, i, j)
    
    return array


parent.check_sort(insertion_sort(parent.generate_array(10000)))
