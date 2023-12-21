from abc import ABC
'''class super_(ABC) : #abstract class as derived from super class like ABC
    id_=1
    name_='rk'
  
ob=super_()
print(ob.id_)
print(ob.name_)'''

'''class super_(ABC) : #abstract class as derived from super class like ABC
  @property
  def name(self) :
    return self.name_
  @name.setter
  def name(self,value) :
    self.name_=value
    
if __name__=='__main__':
  ob=super_()
  ob.name=input(str('Enter name: '))
  print(ob.name)'''


'''class super_(ABC) : #abstract class as derived from super class like ABC
  @property
  def name(self) :
    return self.name_
  @name.setter
  def name(self,value) :
    self.name_=value
  def disp(self,value):
    print(value.upper())
  
    
if __name__=='__main__':
  ob=super_()
  ob.name=input(str('Enter name: '))
  ob.disp(ob.name)'''

'''from abc import ABC

class super_(ABC):
    def __init__(self):
        self._name = None  # Initialize _name attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def disp(self, value):
        print(value.upper())

if __name__ == '__main__':
    ob = super_()
    ob.name = input('Enter name: ')  # Sets the name using the property setter
    ob.disp(ob.name)  # Prints the uppercase value using the disp method'''

'''class father(ABC):
  def car(self):
    print('honda')
class s(father):
  def car(self):
    print('bmw')
    super().car()
class d(father):
  def building(self):
    print('apartment')

if __name__=='__main__':
  print('s')
  ob=father()
  ob.car()
  ob1=s()
  print('d')
  ob1.car()
  ob2=d()
  ob2.building()'''


from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class using ABC
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):  # Subclassing the abstract class
    def make_sound(self):  # Implementing the abstract method
        print("Bark bark!")

class Cat(Animal):  # Another subclass implementing the abstract method
    def make_sound(self):  # Implementing the abstract method
        print("Meow!")

# Instantiating the subclasses
dog = Dog()
cat = Cat()

# Calling the implemented method from each subclass
dog.make_sound()  # Output: Bark bark!
cat.make_sound()  # Output: Meow!
