from test_a.a_3 import x

y = 55


def my_function(k, p):
    return k + p


print(__name__)
if __name__ == '__main__':
    print("This is b_3 file!", my_function(y, x))
