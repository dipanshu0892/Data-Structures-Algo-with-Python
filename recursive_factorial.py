def recursive_factorial(n, last=1):
    if n <= 1:
        return last
    else:
        return recursive_factorial(n - 1, n * last)
