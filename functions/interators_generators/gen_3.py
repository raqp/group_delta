def my_generator():
    i = 0
    while i <= 5:
        yield i
        i += 1
    # return "ERROR"
    yield "Hello"


x = my_generator()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
