# Method Resolution Order

class A:

    x = 10

    def calculate_sum(self, x, y):
        return x + y


class B:

    x = 20

    def mult(self, x, y):
        return x * y


class C(A, B):
    pass


c = C()

print(C.__mro__)
