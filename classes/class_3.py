class Math:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def mult(self):
        return self.x * self.y


math_1 = Math(10, 25)
math_2 = Math(1, 2)

# print(math_1.add())
# print(math_2.mult())
math_1.x = 100

print(math_1.x)

