x = [1, 2, 3, 4, 5]

try:
    y = iter(x)
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
except StopIteration:
    print("StopIteration exception")

