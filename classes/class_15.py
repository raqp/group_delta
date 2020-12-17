class A:

    def __init__(self):
        self.x = 15

    def __add__(self, other):
        return self.x + other

a = A()
print(a + 10)