#inheritance presents reuability status as major features of oops
#inheritance relates with class and interface
#python supports inheritance intelligent ways like 
'''a. single level
b. multi level
c. multiple
d. hybrid'''

'''class kc1:
  pass
ob=kc1()
print(ob)
print(kc1.__bases__,kc1.__base__,kc1.__base__.__base__)'''

#single level inheritance
'''class super_:
  id_=1
  name_='u'
class sub_(super_):
  address_='bbsr'
  sal_=34000
ob=sub_()
print(ob.id_,ob.name_,ob.address_,ob.sal_)'''


'''# Python program to demonstrate
# single inheritance

# Base class
class Parent:
  def func1(self):
    print("This function is in parent class.")

# Derived class


class Child(Parent):
  def func2(self):
    print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2()
'''

'''class super_:
  @property
  def id(self):
    return self.id_
  @id.setter
  def id(self,data):
    self.id_=data

class sub_(super_):
  @property
  def name(self):
    return self.name_

  @name.setter
  def name(self,data1):
    self.name_=data1

ob=sub_()
ob.id=2
ob.name='u'
print(ob.id,ob.name)
    '''


#constructor with inheritance
#constructor as a method cant be inherited but can be initialised through derived class constructor
#which is known as base class initialisation

'''class kc1:
  def __init__(self) :
    print('base class constructor')
class u(kc1):
  pass
ob=u()'''

'''class kc1:
  def __init__(self) :
    print('base class constructor')
class u(kc1):
  def __init__(self):
    print('derived class constructor')
ob=u()
'''
  
'''class kc1:
  def __init__(self) :
    print('base class constructor')
class u(kc1):
  def __init__(self):
    print('derived class constructor')
    super().__init__() #super() in Python is a built-in function used to access methods and properties and constructor from a parent or superclass. It provides a way to delegate method calls to parent classes within a class hierarchy.
ob=u()
'''

'''class kc1:
  def __init__(self) :
    self.name='rakesh'
    print('base class constructor',self.name)
class u(kc1):
  def __init__(self):
    print('derived class constructor')
    super().__init__()
    print(self.name)
ob=u()'''

'''
class kc1:
  def __init__(self) :
    self.name='rakesh'
    print('base class constructor',self.name)
class u(kc1):
  def __init__(self):
    print('derived class constructor')
    kc1.__init__(self)
    print(self.name)
ob=u()'''

#base class initialisation 

'''class kc1:
  def __init__(self,con) :
    self.name='rakesh'
    print('base class constructor',self.name)
    self.con=con
class u(kc1):
  def __init__(self,con):
    print('derived class constructor')
    kc1.__init__(self,con)
    print(self.name)
    print(self.con)
ob=u('uid=system;password=manager')'''


'''class kc1:
  def __init__(self,ds) :
    self.ds=ds
  def disp(self)  :
    for x in self.ds:
      print(x)
class u(kc1):
  def __init__(self,ds):
    kc1.__init__(self,ds)
  def add(self,data):
    self.ds.append(data)
    print('new data created')

ob=u([10,20])
ob.disp()'''

'''class kc1:
  def __init__(self, ds=None):
      if ds is None:
          self.ds = []
      else:
          self.ds = ds

  def disp(self):
      for x in self.ds:
          print(x)

class u(kc1):
  def __init__(self, ds=None):
      super().__init__(ds)

  def add(self, data):
      self.ds.append(data)
      print('new data created')

ob = u([10, 20])
ob.disp()'''

'''#heiarchial inheritance
class parent:
  def __init__(self,msg):
    self.msg=msg
    print(self.msg)

class child(parent):
  def __init__(self,msg):
    super().__init__(msg)
    print(self.msg)
class child1(parent):
  def __init__(self,msg):
    super().__init__(msg)
    print(self.msg)
class child2(parent):
  def __init__(self,msg):
    super().__init__(msg)
    print(self.msg)

if __name__=='__main__':
    ob=child('child1')
    ob1=child1('child2')
    ob2=child2('child3')

# Python program to demonstrate
# Hierarchical inheritance


# Base class
class Parent:
  def func1(self):
    print("This function is in parent class.")

# Derived class1


class Child1(Parent):
  def func2(self):
    print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
  def func3(self):
    print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
'''


'''# Python program to demonstrate
# multilevel inheritance

# Base class


class Grandfather:

  def __init__(self, grandfathername):
    self.grandfathername = grandfathername

# Intermediate class


class Father(Grandfather):
  def __init__(self, fathername, grandfathername):
    self.fathername = fathername

    # invoking constructor of Grandfather class
    Grandfather.__init__(self, grandfathername)

# Derived class


class Son(Father):
  def __init__(self, sonname, fathername, grandfathername):
    self.sonname = sonname

    # invoking constructor of Father class
    Father.__init__(self, fathername, grandfathername)

  def print_name(self):
    print('Grandfather name :', self.grandfathername)
    print("Father name :", self.fathername)
    print("Son name :", self.sonname)


# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
'''

'''class gfather:
  def __init__(self,msg):
    self.msg=msg
    print('grandfather: ',self.msg)
class father(gfather):
  def __init__(self,msg):
    super().__init__(msg)
    print('father: ',self.msg)
class u(father):
  def __init__(self,msg):
    super().__init__(msg)
    print('you: ',self.msg)
if __name__=='__main__':
    ob=u('my data')'''

'''#multiple inheritance

# Parent class 1: Father
class Father:
    def skills(self):
        print("Father's skills: Carpentry, Cooking")

# Parent class 2: Mother
class Mother:
    def skills(self):
        print("Mother's skills: Painting, Singing")

# Child class inheriting from Father and Mother
class Child(Father, Mother):
    pass

# Creating an instance of Child class
child = Child()

# Accessing skills method from Child
child.skills()  # Output will depend on the order of inheritance (see explanation below)'''



'''# Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
  mothername = ""

  def mother(self):
    print(self.mothername)

# Base class2


class Father:
  fathername = ""

  def father(self):
    print(self.fathername)

# Derived class


class Son(Mother, Father):
  def parents(self):
    print("Father :", self.fathername)
    print("Mother :", self.mothername)


# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()'''

'''# Python program to demonstrate
# hybrid inheritance


class School:
  def func1(self):
    print("This function is in school.")


class Student1(School):
  def func2(self):
    print("This function is in student 1. ")


class Student2(School):
  def func3(self):
    print("This function is in student 2.")


class Student3(Student1, School):
  def func4(self):
    print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()
'''
'''
# Parent class 1: Animal
class Animal:
    def eat(self):
        print("Eating...")

# Parent class 2: Bird
class Bird(Animal):
    def fly(self):
        print("Flying...")

# Parent class 3: Fish
class Fish(Animal):
    def swim(self):
        print("Swimming...")

# Child class inheriting from Bird and Fish
class Amphibian(Bird, Fish):
    pass

# Creating an instance of Amphibian class
frog = Amphibian()

# Accessing methods from Bird, Fish, and Animal classes
frog.fly()  # Output: Flying...
frog.swim()  # Output: Swimming...
frog.eat()  # Output: Eating...
'''

class A:
  x=10
class B(A):
  y='rk'
class C(A):
  z='python'
class D(B,C):
  all_='hello'
if __name__=='__main__':
  ob=D()
  print(ob.x)
  print(ob.y)
  print(ob.z)
  print(ob.all_)
