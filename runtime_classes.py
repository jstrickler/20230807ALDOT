
class Animal:
    def move(self):
        print("moving...")

class Cat(Animal):
    def speak(self):
        print("meow")

class_name = "Dog"
parent_class = Animal

def speak(self):
    print("Woof woof")

Dog = type(class_name, (parent_class,), {'speak': speak})

c = Cat()
c.move()
c.speak()
d = Dog()
d.move()
d.speak()