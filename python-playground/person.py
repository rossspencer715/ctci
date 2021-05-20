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
    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name


p = Person("Ross", 24)
print(p.Name)
p.Name = "Efa"
print(p.Name)
p.SayHi()