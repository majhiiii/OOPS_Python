# constructor is a method without return type invokes automatic at the the time of object creation
#python constructor 
'''class Kc_class:
  def __init__(self):
    print("constructor called")
ob=Kc_class()    
ob=Kc_class()    '''


'''class Kc_class:
  x=0
  def __init__(self):
    print("constructor called", Kc_class.x)
    Kc_class.x+=1
ob=Kc_class()    
ob=Kc_class()    
ob=Kc_class()    
ob=Kc_class()    
ob=Kc_class()'''

'''class Kc_class:
  x=0
  def __init__(self):
    print('constructor called {0}'.format (Kc_class.x))
    Kc_class.x+=1
if __name__=='__main__':
      ob=None
      for x in range(5):
         ob=Kc_class()    
     '''


#copy constructors
'''import time
class Kc_class:
  x=0
  def __init__(self):
    print('timer {0}'.format (Kc_class.x))
    Kc_class.x+=1
    time.sleep(1)
if __name__=='__main__':
      ob=None
      for x in range(60):
         ob=Kc_class() '''   


'''import time
class Kc_class:
  x=0
  def __init__(self):
    print('timer {0}'.format (Kc_class.x))
    Kc_class.x+=1
    time.sleep(1)
if __name__=='__main__':
  ob=Kc_class()  
  ob1=ob
  ob2=ob
  ob3=ob
 

import time

class Kc_class:
    x = 0

    def __init__(self):
        print('timer {0}'.format(Kc_class.x))
        Kc_class.x += 1
        time.sleep(1)

    # Copy constructor
    def make_copy(self):
        new_instance = Kc_class()  # Creating a new instance
        new_instance.x = self.x  # Copying the value of 'x'
        return new_instance

if __name__ == '__main__':
    ob = Kc_class()

    # Using the copy constructor to create new instances
    ob1 = ob.make_copy()
    ob2 = ob.make_copy()
    ob3 = ob.make_copy()


import time

class Kc_class:
    def __init__(self, count):
        self.count = count
        print(f"timer {self.count}")
        time.sleep(1)

if __name__ == '__main__':
    # Create separate instances
    ob1 = Kc_class(1)
    ob2 = Kc_class(2)
    ob3 = Kc_class(3)


class Kc_class:
  def __init__(self, x):
      self.x = x

  def __str__(self):
      return f"Kc_class: x = {self.x}"

  # Copy constructor
  def make_copy(self):
      new_instance = Kc_class(self.x)  # Creating a new instance with the same value of 'x'
      return new_instance

if __name__ == '__main__':
  obj1 = Kc_class(5)
  print(obj1)  # Output: Kc_class: x = 5

  obj2 = obj1.make_copy()  # Using the copy constructor
  print(obj2)  # Output: Kc_class: x = 5'''


'''class Kc_class:
  # Class variable initialized to 0
  x = 0

  def __init__(self, connection_string, number):
      # Initializing instance variables with provided values
      self.connection_string = connection_string
      self.number = number

      # Printing the provided values for connection_string and number
      print(self.connection_string, self.number)

if __name__ == '__main__':
  # Creating an instance of Kc_class with sample values
  example_object = Kc_class('uid=system;password=manager', 10)
  #print(example_object)  # Output: uid=system;password=manager 10'''
  
'''class Kc_class:
  x=0
  def __init__(self,con,no):
    if isinstance(con,str) ==True and isinstance(no,int)==True:
      print('Okay')
    else :
      print('enter valid parameter')
  def __init__(self,con,no):
    if isinstance(con,str) ==True and isinstance(no,int)==True:
      print('Okay1')
    else :
      print('enter valid parameter')
if __name__=='__main__':
  ob=Kc_class('uid=system;password=manager',10)
  ob=Kc_class(1,10)
  '''