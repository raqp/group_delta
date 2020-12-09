d = {"name": "John", "job": "developer", "a": "A"}
x = "Hello my name is {name}. I am {job}."

print(x.format(**d))
