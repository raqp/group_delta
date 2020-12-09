x = 5

try:
    print(x)
    print(x / 5)
    print(x + "H")
except (ZeroDivisionError, TypeError):
    print("ZeroDivisionError exception")
except TypeError:
    print("TypeError exception")

print("hello")
