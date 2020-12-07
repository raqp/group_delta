k = [1, 2, 5]


def my_function(x, y, z=23):
    return x + y + z


print(my_function(*k))  # unpack

