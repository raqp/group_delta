import builtins

def my_function():
    global x
    x = 10


my_function()

print(dir(builtins))


