n = int(input("Enter a number: "))
result = 0


def factorial(n):
    global result
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result


print(result)
factorial(n)
