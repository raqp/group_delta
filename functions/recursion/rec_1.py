# x = 6
# f = 1
# for i in range(1, x + 1):
#     f *= i
#
# print(f)


def factorial(x):
    if x == 1:
        return x
    return x * factorial(x - 1)


# 5 * factorial(4) // 5 * 24 = 120
# 4 * factorial(3) // 4 * 6 = 24
# 3 * factorial(2) // 3 * 2 = 6
# 2 * factorial(1) //  2 * 1 = 2
# FILO

print(factorial(5))
