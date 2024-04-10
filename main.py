# Access object attribute by String Name in Python

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name


emp1 = Employee('bobbyhadz', 100)

print(getattr(emp1, 'name'))  # 👉️ bobbyhadz
print(getattr(emp1, 'salary'))  # 👉️ 100