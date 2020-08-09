#Super class
class Animal:
    def __init__(self, animalType = "Undefined", name = "Undefined", age = 1):
        self.__animalType = animalType
        self.__sleeping = False
        self.__name = name
        self.__age = age

    def breathe(self):
        print(self.__animalType+" is breathing")

    def sleep(self):
        self.__sleeping = True

    def wake(self):
        self.__sleeping = False

    def isSleeping(self):
        return self.__sleeping

    def isAwake(self):
        return not self.__sleeping

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def __str__(self):
        return "Animal: "+self.__animalType+" \nName: "+self.__name+" \nAge: "+str(self.__age)+"\n"

#Subclass
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog", name, age)

    def bark(self):
        print(self.getName()+" is barking")

#Subclass
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__("Cat", name, age)

    def meow(self):
        print(self.getName()+" says meow")

a = Dog("Bob", 3)
b = Cat("Dave", 1)
print(a)
print(b)

a.bark()
b.meow()
a.wake()
print(a.getName()+" is sleeping: "+str(a.isSleeping()))
b.sleep()
print(b.getName()+" is sleeping: "+str(b.isSleeping()))

    