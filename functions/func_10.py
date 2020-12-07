def my_function(x, y=[]):
    y.append(x)
    return y


print(my_function(10))
print(my_function(15))
