x = 5


def first_function():
    x = 10

    def second_function():
        nonlocal x
        x += 1
        print(x)

    second_function()
    print(x)


first_function()
print(x)
