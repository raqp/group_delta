class CustomError(Exception):

    def __init__(self, message="My custom Error message"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"This is __str__ magic method! {self.message}"


def my_function(x):
    try:
        if x > 10:
            raise CustomError
        return x ** 2
    except CustomError as e:
        return e

print(my_function(30))
