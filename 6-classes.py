# An example of two classes,
# a child and a parent class.


class Person(object):
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        # The __init__ method defines the parameters necessary to instantiate
        # the Employee object. Notice that you do not have to instantiate
        # a Person and then an Employee. You may simply instantiate a Person
        # and the naming method from Person can be used here as showd below.


        # super() runs the __init__ method from the parent of Employee
        #    In this case, init method from the Person parent class is called.
        #    Note how super() requires "self" but __init__() does not.
        super(Employee, self).__init__(name)

        # The last part of instantiating the Employee class passes the salary
        # parameter to the "self" object of this class.
        self.salary = salary

    def self_print(self):
        print(self)

# Instantiate a couple Persons and an Employee
mary = Person("Mary")
gary = Employee("Gary", 40000)

# Now print some of their values
print(mary.name, "\n")
print(gary.name, "\n")
print(gary.salary, "\n")

# Now run a method that prints the self object
# Note how the self object returns only a pointer.
# I wonder how to print its contents.
gary.self_print()
print("\n")

# As expected from studying Employee's __init__ method, the Employee class will
# fail to instantiate if all required parameters are not passed.
tom = Employee("Tom")
