class Person:

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


john_info = Person(name="John", age=20, job="developer")
john_info.age = 25

robert_info = Person("Robert", 30, "teacher")
print(robert_info.age)
print(john_info.age)

