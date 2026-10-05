cache = {}


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative  number")

    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]
