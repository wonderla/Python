def factorial(n):
    #n! can also be defines as n * (n-1)!
    """ calculates n! recursively"""
    if n<= 1:
        return 1
    else:
        return n * factorial(n-1)
try:
    print(factorial(900))
except (RecursionError, ZeroDivisionError):
    print("This program doesnt do that")
