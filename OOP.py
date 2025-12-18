class Car:
    def __init__(self): #class method
        self.highSpeed="360km/hr"
        self.name="Audi"
    
    def start(self):
        print("Car is getting Started")
    def stop(self):
        print("Car is stopped")
#Car --> 2 Attributes 2 Methods

class Dog(Car):
    def __init__(self): #class method
        self.color="brown"
        self.name="Paapu"
        self.age=1.5
    
    def bark(self):
        print("Bow Bow...!")
#Dog --> 3 Attributes 1 Methods

car1=Car()
dog1=Dog()


print(dog1.name)

# print(car1.name)
# print(car1.highSpeed)
# car1.start()
# car1.stop()

# print(dog1.name)
# print(dog1.age)
# print(dog1.color)
# dog1.bark()


# a="Hello"
# b=[1,2,3,4,5,7]
# c=Dog()

# print(type(c)) #<class '__main__.Dog'>

# Inheritance

a=1
b=2