def factorial(n):
    """Calculate the factorial of n"""
    fac = 1
    for i in range(1, n+1):
        fac = fac*i
    print('the factorial of n is:', fac)
    return fac
