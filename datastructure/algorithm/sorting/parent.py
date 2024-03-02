import random
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir) 

from timer import performance

def check_sort(array):
    l = len(array)
    sortesd = True
    for i in range(l-1):
        if array[i] > array[i+1]:
            sortesd = False
            break
    if sortesd is False:
        print(sortesd)
    else:
        return sortesd

def generate_array(n, printT=False):
    a = [random.randint(1,n) for i in range(n)]
    if printT:
        print(a)
    return a