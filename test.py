# mutable: list, set, dict, bytesarray
# immutable: str, tuple, bytes, frozenset, int, float, complex
# -5, 256

x = [1, 2, 3]
y = x[:]

print(id(x))
print(id(y))

print(x is y)
print(id(x) == id(y))
