def factorial(n):
    global CallNumber
    CallNumber += 1
    print(CallNumber, ' ', n)
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
        print('Return value: ', result)
    return result


CallNumber = 0
print(factorial(3))
