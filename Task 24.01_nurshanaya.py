def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * Factorial(n-1)
    return result
