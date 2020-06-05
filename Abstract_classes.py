'''import keyword
#print(keyword.kwlist)
print(type(1))
print(type([]))
print(type({}))
print(type(()))
print(type(" "))
print(type(keyword))


from abc import ABC,abstractmethod
class bankclass(ABC):                   #abstract class
    @abstractmethod                     #'@" is abbrevation
    def deposit(self,amount):
        pass
class andhrabank(bankclass):
    def example(self):
        print("hi")
    def deposit(self,amount):
        print(amount)
e=andhrabank()'''


from abc import ABC,abstractmethod
class animal(ABC):                   #abstract class
    @abstractmethod                     #'@" is abbrevation
    def walks(self,name):
        pass
class monkey(ABC):
    def walks(self,name):
        print(name," Walks on Two legs and climbs")
class human(ABC):
    def walks(self,name):
        print(name," Walks on only Two legs")
class snake(ABC):
    def walks(self,name):
        print(name," crawls on the ground")
e=monkey()
e.walks("monkey")
e=human()
e.walks("human")
e=snake()
e.walks("snake")
