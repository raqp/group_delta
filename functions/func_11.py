# LEGB
# L - local
# E - enclosing
# G - Global
# B - builtin


x = 10


def function():
    global x
    x += 1
    print(x)


function()
print(x)
