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

class PersonBuilder:
    def __init__(self):
        self.__name = None
        self.__age = None
    def set_name(self, name):
        self.__name = name
        return self
    def set_age(self, age):
        self.__age = age
        return self
    def build(self):
        return Person(self.__name, self.__age)

p = Person("Ross", 24)
print(p.Name)
p.Name = "Efa"
print(p.Name)
p.SayHi()
ltf = LivingThingFactory()
p2 = ltf.make()
print(p2)
p3 = PersonBuilder().set_name("Paul").build()
print(p3)