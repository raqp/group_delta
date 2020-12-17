class Person:

    def __init__(self, name, job, salary):
        self.name = name
        self._job = job
        self.__salary = salary

    def get_salary(self, is_admin=False):
        if is_admin:
            return self.__salary
        else:
            return "Permission denied"


john = Person("John", job="developer", salary="500$")
print(john._job)
print(john.get_salary())
print(john._Person__salary)