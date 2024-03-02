import parent
from timer import performance


@performance
def factorial_recursion(n):
    if n != 1:
        return n * factorial_recursion(n-1)
    elif n == 1:
        return n


@performance
def factorial_loop(n):
    rv = 1
    for i in range(2, n+1):
        rv *= i
    return rv


print(factorial_recursion(50))
print(factorial_loop(50))
