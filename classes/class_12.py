class CustomIterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1


iterator = CustomIterator(10, 15)

for i in iterator:
    print(i)
