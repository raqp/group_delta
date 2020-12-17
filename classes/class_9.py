class A:
    s = 0

    def calculate_sum(self):
        return "Hello"


class B(A):

    def calculate_sum(self, x, y):
        print(x + y)


a = A()
b = B()

print(a.calculate_sum())
b.calculate_sum(10, 25)
