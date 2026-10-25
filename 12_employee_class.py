class Employee:
    count = 0  # counts the number of objects created

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print("Name:", self.name, "| Salary:", self.salary)


e1 = Employee("Rahul", 30000)
e2 = Employee("Priya", 45000)
e3 = Employee("Aman", 38000)

e1.display()
e2.display()
e3.display()

print("Total number of employees:", Employee.count)
