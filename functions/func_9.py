def my_function(x, y, *args, **kwargs):
    print(x, y)
    print(args)
    print(kwargs)


my_function(1, 2, 3, 4, 5, t=10, p=50, h="Hello")
