def fact(n):
    if n == 1:
        return 1
    else:
        result = n * fact(n - 1)
        return result