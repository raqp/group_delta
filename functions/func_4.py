def my_function(x, y=5, z=None, k=None):
    if z and k:
        return x ** y, y ** x, z ** k
    return x ** y, y ** x


print(my_function(y=4, x=2, z=3, k=5))
