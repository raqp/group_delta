class A:

    x = 20

    def calculate_sum(self, x, y):
        return x + y


class B:

    x = 10

    def mult(self, x, y):
        return x * y


class C(A, B):
    pass


c = C()

print(c.x)