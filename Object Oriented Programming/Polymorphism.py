# Polymorphism: One thing existing in several forms. Poly means 'many' morphism means 'forms'.
# Example: There is one person who can do multiple things.

class Cat:
    def speak(self):
        print("Meow Meow")


class Dog:
    def speak(self):
        print("Bhaw Bhaw")


def animal_sound(animal):
    return animal.speak()


cat = Cat()
dog = Dog()

print(animal_sound(cat))
print(animal_sound(dog))