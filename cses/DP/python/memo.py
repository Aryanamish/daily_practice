import functools


def memoize(parameter_names):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create a tuple of arguments based on the specified parameter names
            memoize_key = tuple(kwargs[param] for param in parameter_names)

            if memoize_key not in wrapper.cache:
                # If the result is not cached, compute and cache it
                result = func(*args, **kwargs)
                wrapper.cache[memoize_key] = result

            # Return the cached result
            return wrapper.cache[memoize_key]

        # Initialize a cache dictionary for the wrapper function
        wrapper.cache = {}

        return wrapper
    return decorator

# Example usage:


if __name__ == '__main__':
    @memoize(("x", "y", 'z'))
    def add(x, y, z):
        print(f"Calculating {x} + {y} + {z}")
        return x + y + z

    # Now, the "add" function is memoized based on the parameters "x" and "y"
    result1 = add(x=2, y=3, z=10)
    result2 = add(x=2, y=3, z=15)  # This will use the cached result

    print(result1)  # Output: Calculating 2 + 3\n5
    print(result2)  # Output: 5 (This uses the cached result)
