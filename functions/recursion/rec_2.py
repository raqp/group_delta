# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


def fib(x):
    if x <= 2:
        return 1
    return fib(x - 1) + fib(x - 2)


# fib(5) = fib(4) + fib(3)  // fib(5) = 3 + 2 = 5
# fib(4) = fib(3) + fib(2)  // fib(4) = 2 + 1 = 3
# fib(3) = fib(2) + fib(1)  // fib(3) = 1 + 1 = 2

# fib(3) = fib(2) + fib(1)  // fib(3) = 1 + 1 = 2


print(fib(5))
