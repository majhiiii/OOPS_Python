#method 

'''class Kc_class:
    x=0
    def __init__(self):
      self.ds=[]
    def additem(self,data)  :
      self.ds.append(data)
      print('item added')
    def removeitem(self,data):
      if data in self.ds:
        self.ds.remove(data)
        print('item removed')
      else:
        print('item not found')  

    def disp(self):
      for x in self.ds:
        print(x)

ob=Kc_class()
ob.additem('a')
ob.additem('b')
ob.additem('c')
ob.additem('d')
ob.additem('e')
ob.disp()
ob.removeitem('a')
ob.disp()
'''

'''class Kc_class:
  x=0
  def __init__(self):
    self.ds=[]
  def additem(self,data)  :
    self.ds.append(data)
    print('item added')
  def removeitem(self,data):
    if data in self.ds:
      self.ds.remove(data)
      print('item removed')
    else:
      print('item not found')  

  def disp(self):
    for x in self.ds:
      print(x)

  def data_(self,*args):
    print(args)
    print(type(args))
    for x in args:
      self.ds.append(x)
      print(x)

ob=Kc_class()
ob.data_('a','b','c','d','e')'''


'''class Kc_class:
  x=0
  def __init__(self):
    self.ds=[]
  def additem(self,data)  :
    self.ds.append(data)
    print('item added')
  def removeitem(self,data):
    if data in self.ds:
      self.ds.remove(data)
      print('item removed')
    else:
      print('item not found')  

  def disp(self):
    for x in self.ds:
      print(x)

  def data_(self,*args):
    print(args)
    print(type(args))
    for x in args:
      self.ds.append(x)
      print(x)

  def data1_(self,**args):
    print(args['name'])

ob=Kc_class()
ob.data_('a','b','c','d','e')
ob.data1_(name='rakesh')


class Kc_class:
  x = 0

  def __init__(self):
      self.ds = []

  def operate_item(self, data, action='add'):
      if action == 'add':
          self.ds.append(data)
          print('Item added')
      elif action == 'remove':
          if data in self.ds:
              self.ds.remove(data)
              print('Item removed')
          else:
              print('Item not found')
      else:
          raise ValueError("Invalid action. Use 'add' or 'remove'.")

  def disp(self):
      for x in self.ds:
          print(x)

  def data_(self, *args):
      print(args)
      print(type(args))
      for x in args:
          self.operate_item(x, 'add')
          print(x)

  def data1_(self, **kwargs):
      if 'name' in kwargs:
          print(kwargs['name'])
      else:
          print("Key 'name' not found in arguments.")


ob = Kc_class()
ob.data_('a', 'b', 'c', 'd', 'e')
ob.data1_(name='rakesh')

class Kc_class:
  x = 0

  def __init__(self):
      self.ds = []

  def add_item(self, data):
      self.ds.append(data)
      print('Item added')

  def remove_item(self, data):
      if data in self.ds:
          self.ds.remove(data)
          print('Item removed')
      else:
          print('Item not found')

  def display_items(self):
      for item in self.ds:
          print(item)

  def add_items(self, *args):
      print(args)
      print(type(args))
      for item in args:
          self.ds.append(item)
          print(item)

  def print_name(self, **kwargs):
      if 'name' in kwargs:
          print(kwargs['name'])

  def get_info(self, data):
      return data

  def calculate_factorial(self, num):
      if num == 0:
          return 1
      else:
          return num * self.calculate_factorial(num - 1)


ob = Kc_class()
ob.add_items('a', 'b', 'c', 'd', 'e')
ob.print_name(name='rakesh')
print(ob.get_info('majhi'))

# Taking user input for factorial calculation
user_input = input("Enter a number to calculate its factorial: ")

if user_input.isdigit():
  num = int(user_input)
  factorial = ob.calculate_factorial(num)
  print(f"The factorial of {num} is: {factorial}")
else:
  print("Please enter a valid integer for factorial calculation.")


'''



'''class Kc_class:
  x=0
  def __init__(self):
    self.ds=[]
  def additem(self,data)  :
    self.ds.append(data)
    print('item added')
  def removeitem(self,data):
    if data in self.ds:
      self.ds.remove(data)
      print('item removed')
    else:
      print('item not found')  

  def disp(self):
    for x in self.ds:
      print(x)

  def data_(self,*args):
    print(args)
    print(type(args))
    for x in args:
      self.ds.append(x)
      print(x)

  def data1_(self,**args):
    print(args['name'])

  def info(self,data3):
    return data3
  def fact(self,x):
    if x==0:
      return 1
    else:
      return x*self.fact(x-1)
ob=Kc_class()
ob.data_('a','b','c','d','e')
ob.data1_(name='rakesh')
print(ob.info('majhi'))
print(ob.fact(5))'''

#method with entity parameter


class emp:
  def __init__(self,id_,name_,city_):
    self.id=id_
    self.name=name_
    self.city=city_
class Kc_class:
  x=0
  def __init__(self):
    self.ds=[]
  def additem(self,data)  :
    self.ds.append(data)
    print('item added')
  def removeitem(self,data):
    if data in self.ds:
      self.ds.remove(data)
      print('item removed')
    else:
      print('item not found')  

  def disp(self):
    for x in self.ds:
      print(x.id,x.name,x.city)


ob=Kc_class()
ob.additem(emp(1,'rakesh','delhi'))
ob.additem(emp(2,'ankit','bbsr'))
ob.additem(emp(3,'hari','bbsr'))
ob.disp()