class A:
    s = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def mult(x, y):
        return A.s + x + y


class B(A):

    def calculate_sum(self, x, y):
        print(x + y)


print(A.mult(2, 5))
