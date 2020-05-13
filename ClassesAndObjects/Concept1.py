class Employee:
    raise_amount = 1.04
    num_empls = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '' + last + '@company.com'
        Employee.num_empls += 1  # Incrementing the value to count the number of employees instances created.

    def rtn_data(self):
        return '{} {} salary is {}. Has email: {}'. \
            format(self.first, self.last, self.pay, self.email)

    @classmethod
    def set_amount(cls, amount):
        cls.raise_amount = amount
        # cls is the default python variable for class.

    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):  # Inheriting the Employee class
    raise_amount = 1.10  # Overrding the employees raiseamount variable
    num_devs = 0

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        Developer.num_devs += 1

    def rtn_data(self):
        return '{} {} salary is {}. Has email: {}. Skilled in {} Programming'. \
            format(self.first, self.last, self.pay, self.email, self.prog_lang)

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee("Irfan", "Khan", 40000)
emp_2 = Employee("Farhan", "Khan", 50000)

print("Number of Employees created: ", + Employee.num_empls)
print(emp_1.rtn_data())
print(emp_2.rtn_data())

# Using __dict__ method to get the data as list of any object.
print(emp_1.__dict__)
# The return in output is the amount raised to 41600 because
# the call to function raise_pay() has done and the pay value got changed.

Employee.set_amount(5.0)

emp_3 = Employee("Sidra", "Khan", 20000)
# After calling the raise_pay method, the raise_amount is set to 5 and
# the salary increased 5 times of 20000.
emp_3.raise_pay()
print(emp_3.pay)

dev_1 = Developer("Rahman", "Fasi", 80000, "Java")
dev_2 = Developer("Uneera", "Syeda", 70000, "Python")

print("Number of Developers created: ", + Developer.num_devs)
print(dev_1.rtn_data())
print(dev_2.rtn_data())

total_employees = Employee.num_empls + Developer.num_devs
print("Total Employees:", + total_employees)

# Below function checks whether the object belongs to class or not.
print(isinstance(dev_1, Developer))

# Below function checks whether the class is a subclass of another (second arg).
print(issubclass(Developer, Employee))


# Below function gives the description of the class, parent class, associated attributes etc.
# print(help(Developer))


## Special Methods/Dunder Methods #############

def __repr__(self):
    pass


def __str__(self):
    pass

print(len('irfankhan'))
#or
print('irfankhan'.__len__())

print(repr(dev_1))
print(dev_1.__str__())

# In built dunder methods
print(1 + 2)
print(int.__add__(1, 2))

print('a' + 'b')
print(str.__add__('a', 'b'))

# Calling __add__() method to add salaries
# of two employees or developers.
print(dev_1 + dev_2)


###################################################################################
# Redundant Code

# emp_1.raise_pay()
# print(emp_1.pay)
# emp_4 = Employee
# emp_4.pay = 500
# emp_4.set_amount(6)
# # Accessing the classmethod variable with a class variable.
#
# Employee.raise_pay(emp_4)
#
# print(emp_4.pay)
# Employee.set_amount(8)
# print(Employee.raise_amount)
