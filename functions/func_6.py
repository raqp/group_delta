x = {"z": 1, "k": 2, "t": 3}


def my_function(y, z, k):
    print("y:", y)
    print("z:", z)
    print("k:", k)
    return z * k * y


print(my_function(**x))
