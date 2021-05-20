import abc

class LivingThing(metaclass=abc.ABCMeta):
    @abc.abstractstaticmethod
    def SayHi(self):
        print("Hi there")


class Person(LivingThing):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def SayHi(self):
        print("Hi, I'm a person")
    def __repr__(self):
        return f"My name is {self.__name} and I'm {self.__age} years old"
    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name


class LivingThingFactory:
    def __init__(self):
        pass
    def make(self):
        tp = input("Type of living thing: ")
        nm = input("Name: ")
        age = input("Age: ")
        if tp == "Person":
            return Person(nm, age)

p = Person("Ross", 24)
print(p.Name)
p.Name = "Efa"
print(p.Name)
p.SayHi()
ltf = LivingThingFactory()
p2 = ltf.make()
print(p2)