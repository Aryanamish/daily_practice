import time


def performance(p=False):
    if callable(p):
        fun = p
        def wrapper(*args, **kwargs):
            t = time.time()
            a = fun(*args, **kwargs)
            print(f"time taken for function `{fun.__name__}` is {time.time() - t} seconds")
            return a
        return wrapper
    def decorator(fun):
        def wrapper(*args, **kwargs):
            t = time.time()
            a = fun(*args, **kwargs)
            if p is True:
                print(a)
            print(f"time taken for function `{fun.__name__}` is {time.time() - t} seconds")
            return a
        return wrapper
    return decorator