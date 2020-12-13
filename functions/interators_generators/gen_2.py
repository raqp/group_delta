def my_generator():
    i = 0
    while i <= 10:
        yield i
        i += 1


for j in my_generator():
    print(j)
