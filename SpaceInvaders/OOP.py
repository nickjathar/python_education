class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I haven't learned how to speak yet!")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meowwwww")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")

class Dog(Pet):
    def speak(self):
        print("Woooooof")

class Fish(Pet):
    pass

class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod
    def display_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

class Math:

    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")

p = Pet("Tim", 19)
p.speak()

c = Cat("Bill", 36, "Brown")
c.show()
c.speak()

d = Dog("Jill", 25)
d.speak()

f = Fish("Bubbles", 2)
f.speak()

p1 = Person("Tim")
print(Person.number_of_people)
print(p1.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)
print(p1.number_of_people)

# Person.number_of_people = 8
# print(Person.number_of_people)

p3 = Person("Nick")
print(Person.number_of_people)
print(p1.number_of_people)

p4 = Person("Raina")
print(Person.display_number_of_people())

print(Math.add5(6))
print(Math.add10(6))
Math.pr()