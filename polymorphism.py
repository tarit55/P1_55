class Animal:
    def speak(self):
        return "Animal makes  sound"

class Dog(Animal):
    def speak(self):
        return "Dog says woof"

class Cat(Animal):
    def speak(self):
        return "Cat says meow"

class Wolf(Animal):
    def speak(self):
        return "Wolf says howl"

def animal_sound(animal):
    print(animal.speak())

animal1 = Dog()
animal2 = Cat()
animal3 = Wolf()

animal_sound(animal1)  
animal_sound(animal2)   
animal_sound(animal3)  