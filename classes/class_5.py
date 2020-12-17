class A:

    def say_hello(self):
        return "Hello"


class B(A):

    def say_bye(self):
        return "Bye"


b = B()

print(b.say_hello())
