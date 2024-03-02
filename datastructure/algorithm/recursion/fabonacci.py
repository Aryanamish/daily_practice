import parent

from timer import performance

def fabonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fabonacci_recursive(n-1) + fabonacci_recursive(n-2)

@performance
def febonacci_itrative(n):
    second_last = 0
    last = 1
    n = n-2
    while n >= 0:
        last, second_last = second_last+last, last
        n -= 1
    return repr(last)

f = performance(fabonacci_recursive)
febonacci_itrative(300000)
performance(fabonacci_recursive)(300000)



