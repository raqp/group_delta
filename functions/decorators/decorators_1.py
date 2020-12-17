def decorator_function(function):
    def second_function():
        print(1)
        function()
        print(2)

    return second_function


@decorator_function
def my_function():
    print("Hello World!")


my_function()
