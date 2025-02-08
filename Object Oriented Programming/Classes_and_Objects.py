# Paradigms
# It's a principle according to which a program organized to carry out given task.

# Procedural Programming
# Functional Programming
# Object-Oriented Programming

# Advantage of OOP over other paradigms
# Code reputation
# Code organized
# Easy large projects programs
# Blueprint of things that needed to be done.

# Car: Nano => Design(Blueprint) => 3,000

# Class: A class contains data and methods that can access or manipulate this data. Class let us bundle data and
# functionality together.

# Nano: blueprint : Material(data) | machines(methods)

# Object: Original document => photo copy

# Example: Birds(Class): Crow, Eagle
#          Humans(Class): Abhay, Himanshu

# i = 10 # i is an object of int class
# i = 1.9 # i is an object of float class

human1 = 'Naruto'
human2 = 'Sasuke'

human1.capitalize()
human2.capitalize()


# Public and Private Members

# Members of a class(data and methods) are accessible from outside the class.
# Private members convention : starts with an underscore
# 3 private member 2 public method
class Employee:
    def __init__(self):
        self._name = None
        self._age = None
        self._salary = None

    def set_data(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def display_data(self):
        print(self._name, self._age, self._salary)


# Object creation
emp1 = Employee()
emp1.set_data('Naruto', 21, 120000)


# emp1.display_data()


# object --call--> method --address emp1--> Employee() ---> self
# Properties / Attributes
# Methods / Behaviour

# Object Initialization
class Employee:
    """This is employee class"""

    def __init__(self, name='', age=0, salary=0):  # __init__ not give any o/p, will call only 1 time
        self._name = name
        self._age = age
        self._salary = salary

    def set_data(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def display_data(self):
        print(self._name, self._age, self._salary)

    def __del__(self):
        print('Deleting object' + str(self))


# ramesh = Employee('Ramesh', 30, 120000)  # gurenteed initialization
# ramesh.display_data()

# himanshu = Employee()
# himanshu.set_data('Himanshu', 25, 30000)
# himanshu.display_data()

# constructor & destructor
# class attribute / variable

# Global functions
# vars() and dir()
# vars() => returns a dictionary of attributes and their values
# dir() => returns a list of attributes

# print(vars(Employee))

"""
    Question 1: Write a class called Number which maintains an integer. It should have following methods in it to perform various operations on the int:
        set_number(self, n)
        get_number(self, n)
        print_number(self)
        isnegative(self)
        isdivisibleby(self)
        absolute_value(self) 
"""


class Number:
    def __init__(self):
        self.number = 0

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def print_number(self):
        print(self.number)

    def isnegative(self):
        if self.number < 0:
            return True
        else:
            return False

    def isdivisibleby(self, divisible_by):
        if divisible_by == 0:
            return False
        if self.number % divisible_by == 0:
            return True
        else:
            return False

    def absolute_value(self):
        if self.number >= 0:
            return self.number
        else:
            return -1 * self.number


objectA = Number()
objectA.set_number(-11111)
# objectA.print_number()
# print(objectA.absolute_value())

"""
    Question 2: Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use it to perform complex number addition, subtraction, multiplication and division.
"""


class Complex:
    """Complex number follows this format : a + bi where a and b are real and i is imaginary."""

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def addition(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"

    def subtraction(self, other):
        return f"{self.real - other.real} - {self.imaginary - other.imaginary}i"

    def multiplication(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        # real = 5 * 3 - 2 * 5 => 15 - 10 => 5
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        # imaginary => 5 * 5 + 2 * 3 => 25 + 6 => 31
        return f"{real} + {imaginary}i"  # 5 + 31i

    def division(self, other):
        # (a+bi)/(c+di) = [(ac+bd) + (bc-ad)i] / (c^2+d^2)
        denominator = other.real ** 2 + other.imaginary ** 2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return f"{real_part} + {imaginary_part}i"


"""
    Question 3: Write a program that implements a Matrix class and performs addition, multiplication, and transpose operations on 3 x 3 matrices.
"""


class Matrix:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def addition(self):
        addition_matrix = [[self.data1[i][j] + self.data2[i][j] for j in range(3)] for i in range(3)]
        return addition_matrix

    def subtraction(self):
        subtraction_matrix = [[self.data1[i][j] - self.data2[i][j] for j in range(3)] for i in range(3)]
        return subtraction_matrix

    def multiplication(self):
        multiplication_matrix = [[self.data1[i][j] * self.data2[i][j] for j in range(3)] for i in range(3)]
        return multiplication_matrix

    def transpose(self):
        transposed_matrix = [[self.data1[j][i] for j in range(3)] for i in range(3)]
        return transposed_matrix

    def display(matrix):
        for row in matrix:
            print(' '.join(map(str, row)))


# print(f'Enter the input for 3 x 3 matrix')
# matrix1 = [[int(input()) for _ in range(3)] for _ in range(3)]
# matrix2 = [[int(input()) for _ in range(3)] for _ in range(3)]

# class_instance = Matrix(matrix1, matrix2)
# Matrix.display(class_instance.data1)
# Matrix.display(class_instance.data2)
# Matrix.display(class_instance.addition())
# Matrix.display(class_instance.subtraction())
# Matrix.display(class_instance.multiplication())
# Matrix.display(class_instance.transpose())


"""
    Question 3: Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevent to the solid.
"""

import math


class Solid:
    """
        Cube, Sphere, Cylinder
        Cube: surface area: 6 * a^2, volume : a^3
        Sphere: surface area: 4* pie * r^2, volume: 4/3*pie*r^3
        Cylinder: surface area: 2 * pie * r * h + 2 * pie * r^2, volume: pie * r^2 * h
    """

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def surface_area(self):
        if self.shape_type == 'cube':
            side = self.dimensions.get('side')
            return 6 * (side ** 2)
        elif self.shape_type == 'sphere':
            radius = self.dimensions.get('radius')
            return 4 * math.pi * (radius ** 2)
        elif self.shape_type == 'cylinder':
            radius = self.dimensions.get('radius')
            height = self.dimensions.get('height')
            return 2 * math.pi * radius * (radius + height)
        else:
            return "Shape not supported"

    def volume(self):
        if self.shape_type == 'cube':
            side = self.dimensions.get('side')
            return side * side * side
        elif self.shape_type == 'sphere':
            radius = self.dimensions.get('radius')
            return (4 * math.pi * (radius ** 3)) / 3
        elif self.shape_type == 'cylinder':
            height = self.dimensions.get('height')
            radius = self.dimensions.get('radius')
            return math.pi * (radius ** 2) * height
        else:
            return "Shape not supported"


# cube = Solid('cube', side=4)
# print(cube.surface_area())
# print(cube.volume())
# sphere = Solid('sphere', radius=4)
# print(sphere.volume())

"""
    Question 4: Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape.
"""


class Shape:
    """
        Circle: Circumference: 2 * pi * radius, Area = pi * radius**2
        Square: Circumference: 4* side, Area: side**2
    """

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def circumference(self):
        if self.shape_type == 'circle':
            radius = self.dimensions.get('radius')
            return 2 * math.pi * radius
        elif self.shape_type == 'square':
            side = self.dimensions.get('side')
            return 4 * side
        else:
            return "Shape not supported"

    def area(self):
        if self.shape_type == 'square':
            side = self.dimensions.get('side')
            return side ** 2
        elif self.shape_type == 'circle':
            radius = self.dimensions.get('radius')
            return math.pi * radius ** 2
        else:
            return "Shape not supported"


# square = Shape('square', side=2)
# print(square.circumference())
# print(square.area())
# circle = Shape('circle', radius=4)
# print(circle.circumference())
# print(circle.area())


# Python Standards
"""
- Class names start with a uppercase letter
- All other identifier start with lowercase letter
- Private identifier start with leading underscore
"""


# Operator Overloading

class ComplexNumber:
    def __init__(self, r=0.0, i=0.0):
        self._real = r
        self._imaginary = i

    def __add__(self, other):
        z = ComplexNumber()
        z._real = self._real + other._real
        z._imaginary = self._imaginary + other._imaginary
        return z

    def __sub__(self, other):
        z = ComplexNumber()
        z._real = self._real - other._real
        z._imaginary = self._imaginary - other._imaginary
        return z

    def display(self):
        print(f'{self._real} - {self._imaginary}i')


c1 = ComplexNumber(1.1, 0.2)
c2 = ComplexNumber(1.1, 0.2)
#
c3 = c1 - c2
# c3.display()

# In python every entity is an object.
# int, float, string, list, tuple, set
c = (1,2,3,4,5,6)
d = [1,2 ,'a','b']
print(type(list))
print(type(c))
print(type(d))
print(type(float))


