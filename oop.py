class Animals:      #declare class
    def __init__(self, name, food, sound, digits):       #initializer for attributes
        self.food = food        #instance variables
        self.name = name
        self.sound = sound
        self.digits = digits
    def summarized(self):           #intializing a method
        return f"A {self.name} is an animal that {self.sound}s all day, moves around in its {self.digits} just to eat {self.food}"
    
anim_1 = Animals("Dog", "meat", "bark", "paws")
print(anim_1.summarized())
print(Animals.summarized(anim_1))


class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age=99):
        self.call = name
        self.duration = age
    def greet(self):
        return f"Hello, my name is {self.call} and I am {self.duration} years old"
p1 = Person("John", 36)
p2 = Person("Akerele")
print(p1.greet())
print(p2.greet())


def main():                                 #declare main function
    myCount = Count()                       #instance variable under class Count with no argument
    times = 0                               #regular variable assigned

    for i in range(0, 10):                     #iterating whatever condition 100 times
        increment(myCount, times)               #performs increment function 100 times

    print("myCount.count =", myCount.count, "times =", times)               #printing to console the incremented count attribute and incremented times

def increment(c, times):            #declare increment attribute
    c.count += 1                    #count attribute of any object called increments
    times += 1                      #times incremented
    print(times, c.count)

class Count:
    def __init__(self):
        self.count = 0
    
main()



# Create the Dog class
class Dog:
    def __init__(self, name, age):
        self.call = name
        self.time = age
    def bark(self):
        return  f"{self.call} says Woof!" 
# Create an object
d1 = Dog("Buddy", 3)
# Call the bark method
print(d1.bark())

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

class Interface():
    def __init__(slef, name, status, ip_a: str):
        slef.called = name
        slef.state = status
        slef.proxy = ip_a

    def user_message(sleff):
        return "Welcome " + sleff.called + "!"
    def server_store(kai):
        return f'"{kai.user_message()}" was delivered to user. \n User IP = {kai.proxy}'
    
client1 = Interface("Elias", "active", "101.23.4.9.88")
print(client1.server_store())