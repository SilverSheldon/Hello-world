def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n=n-1)

print(factorial(n=3))
print(factorial(n=4))
print(factorial(n=5))
