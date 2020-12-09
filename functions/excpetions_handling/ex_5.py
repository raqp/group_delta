def function(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return e
    except TypeError as e:
        return e
    except Exception as e:
        return e
    finally:
        try:
            x = [1, 2, 3]
            print(x[5])
        except IndexError as e:
            print(e)


print(function(10, 5))
