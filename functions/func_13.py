def first_function():
    x = 10

    def second_function():
        a = "Hello"

        def third_function():
            nonlocal x
            x += 1
            print(x)

        third_function()

    second_function()


first_function()
