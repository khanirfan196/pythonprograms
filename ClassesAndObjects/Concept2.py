# Demonstration of using @property decorator
# Demonstration of Setters and Getters

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name_args):
        first, last = name_args.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Names Deleted !!")
        self.first = None
        self.last = None

emp_1 = Employee("irfan", "khan")

print(emp_1.email)
print(emp_1.fullname)
print()
emp_1.fullname = 'Sidra Khan'
print("After setting the new name:")
print()
print(emp_1.email)
print(emp_1.fullname)
print()

del emp_1.fullname
print("Names after deleting..")
print(emp_1.fullname)