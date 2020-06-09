memo = {}


def fibonacci(n: int):
    if n <= 0:
        return 0
    elif n in [1, 2]:
        return 1
    elif n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
