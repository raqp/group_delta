class ABC:

    def __init__(self, x):
        self.x = x


class B(ABC):

    def __init__(self, y, x):
        super().__init__(x)
        self.y = y


b = B(10, 20)
print(b.x)
