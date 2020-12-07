def my_function(*args):
    x = []
    for i in args:
        x.append(i ** 2)
    return x


print(my_function(1, 2, 3, 4, 5, 6, 7, 8, 9))
