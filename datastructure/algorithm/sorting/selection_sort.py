import parent
import random
from timer import performance

@performance
def selection_sort(array):
    len_array = len(array)
    for i in range(len_array-1):
        smallest = [array[i], i]
        for j in range(i+1, len_array):
            if array[j] < smallest[0]:
                smallest = [array[j], j]
        array[smallest[1]], array[i] = array[i], array[smallest[1]]
    return array


a = [random.randint(1,10000) for i in range(10000)]
selection_sort(a)
parent.check_sort(a)
# selection_sort(a)