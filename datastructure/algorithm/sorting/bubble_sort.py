import parent
import random
from timer import performance


@performance
def bubble_sort(array):
    len_array = len(array)
    for i in range(len_array-1):
        for j in range(0, len_array-1):
            if  array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        
    return array

a = [random.randint(1,100) for _ in range(10000)]
# a = [random.randint(1,100) for _ in range(10)]
# print(a)
bubble_sort(a)
parent.check_sort(a)
# print(bubble_sort(a))