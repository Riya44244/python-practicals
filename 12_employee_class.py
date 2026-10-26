# Practical 12: Employee class
import sys


class Employee:
    count = 0  # number of objects created

    def __init__(self, empno, name, dept, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            print("Error: Basic, DA and HRA cannot be negative. Terminating.")
            sys.exit()
        self.empno = empno
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra
        Employee.count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        type(self).count -= 1

    def __str__(self):
        return ("Employee No : " + str(self.empno) + "\n"
                "Name        : " + self.name + "\n"
                "Department  : " + self.dept + "\n"
                "Basic       : " + str(self.basic) + "\n"
                "DA          : " + str(self.da) + "\n"
                "HRA         : " + str(self.hra) + "\n"
                "Salary      : " + str(self.salary()))


e1 = Employee(101, "Rahul", "Sales", 30000, 5000, 8000)
e2 = Employee(102, "Priya", "HR", 40000, 6000, 10000)

print(e1)
print()
print(e2)
print("\nNumber of employees:", Employee.count)

del e2
print("After deleting one object, number of employees:", Employee.count)

# Uncomment the next line to test the negative value check
# e3 = Employee(103, "Aman", "IT", -100, 500, 500)
