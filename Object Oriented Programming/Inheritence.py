# Reuse Mechanism

# Instead of reinventing the same code that is already available, it makes sense to reuse the existing code.

# 2 type reuse mechanism: Inheritance and Containership(Composition)

# Contaniership
# Container: A container can contain one or more contained objects apart from other data.

class Department:
    def set_department(self):
        self._id = input("Enter department id: ")
        self._name = input("Enter department name: ")

    def display_department(self):
        print("Department ID: " + self._id)
        print("Department Name: " + self._name)


class Employee:
    def set_employee(self):
        self._eid = input("Enter employee id: ")
        self._ename = input("Enter employee name: ")
        self._dobj = Department()
        self._dobj.set_department()

    def display_employee(self):
        print("Employee ID: ", self._eid)
        print("Employee Name: ", self._ename)
        self._dobj.display_department()


# Inheritance
# base class: original class | super class or parent class
# derived class: class that inherit base class | sub class or child class

# base class

class Index:
    def __init__(self):
        self._count = 0

    def display_index(self):
        print('count=' + str(self._count))

    def increase(self):
        self._count += 1


# derived class

class NewIndex(Index):
    def __init__(self):
        super().__init__()

    def decrease(self):
        self._count -= 1


i = NewIndex()


# i.increase()
# i.increase()
# i.increase()
# i.decrease()
# i.display_index()


# isinstance and issubclass()
# print(isinstance(i, NewIndex))
# print(issubclass(NewIndex, Index))

# Type of Inheritance
# 1. Single: base class ---> derived class
# 2. Multilevel: base class ---> derived class ---> derived class
# 3. Multiple: base class A + base class B ---> derived class
# 4. Hierarchical: base class A --> multiple derived classes
# 5. Hybrid: collection of all types of inheritance

class Product:
    def __init__(self):
        self.title = input("Enter product title: ")
        self.price = input("Enter product price: ")

    def display_product(self):
        print("Title: " + self.title)
        print("Price: " + self.price)


class Sales:
    def __init__(self):
        self.sales_figures = [int(x) for x in input("Enter sales fig: ").split()]

    def display_sales(self):
        print("Sales figures:", self.sales_figures)


class HardwareItem(Product, Sales):
    def __init__(self):
        Product.__init__(self)
        Sales.__init__(self)
        self.category = input("Enter product category: ")
        self.oem = input("Enter product oem: ")

    def display_data(self):
        Product.display_product(self)
        Sales.display_sales(self)
        print(self.category, self.oem)


# Dimond Problem
# 2 classes: Derived 1, Derived 2 | Base
# Der | Derived 1, Derived 2

"""        Base
        
    Derived1    Derived2

            Der
            
    def __init__(self):
        super().__init__()
"""
