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
        print("Finally block")


print(function(1, "y"))
