x = {"a": "A"}

try:
    print(5 + "H")
except KeyError:
    x["b"] = "B"
except TypeError as message:
    print(message)
except Exception:
    print("Exception")

print(x)