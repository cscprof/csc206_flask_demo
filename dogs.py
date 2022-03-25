
# Base class for dogs
class Dog:
    species = "Canis familiaris"
    name = ""
    age = -1

    # constructor function
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # dunder method to print "friendly view of class
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # instance method to make the dog speak
    def speak(self, sound):
        return f"{self.name} says {sound}"    


# Class for hunting dogs
class Hunter(Dog):
    prey = "None"

    # constructor function
    def __init__(self, name, age, prey):
        Dog.__init__(self, name, age)
        self.prey = prey

    # dunder method to print "friendly view of class
    def __str__(self):
        return f"{self.name} is {self.age} years old and chases {self.prey}"


# Class for working dogs
class Worker(Dog):
    endurance = 0

    # constructor function
    def __init__(self, name, age, endurance):
        Dog.__init__(self, name, age)
        self.endurance = endurance

    # dunder method to print "friendly view of class
    def __str__(self):
        return f"{self.name} is {self.age} years old and works for {self.endurance} hours"

    # Override the speak method 
    def speak(self, sound):
        return f"{self.name} says {sound} and wakes up the whole neighborhood"

a = Dog("Abbie", 13)
r = Worker("Reagan", 3, 5)

f = Hunter("Killer", 5, "Rabbits")

# print (r)
# print(r.speak("BARK!!!!"))

print (r)
print(r.speak("WOOF!!!!"))

