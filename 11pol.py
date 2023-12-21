'''class Urapp:
  def disp(self):
    print('super class')

class app (Urapp):
  def details(self):
    print('ur data')

if __name__=='__main__':
  ob=app()             # early binding compile time polymorphism
  ob.disp()
  ob.details()'''

'''class Urapp:
  def disp(self):
    print('super class')

class app (Urapp):
  def details(self):
    print('ur data')

if __name__=='__main__':
  ob=None         #late binding
  option= input('enter choice :')
  if option== 'urapp':
    ob=Urapp()
    ob.disp()
  elif option== 'app':
    ob=app()
    ob.disp()
    ob.details()
  else:
    print('invalid option')'''

#class based polymorphism
#method overriding
'''class A:
  def msg(self):
    print('Hello')
  def data(self):
    print('Rakesh')

class B:
  def msg(self):
    print('Hi')
  def data(self):
    print('sai')


ob=A()
ob1=B()
for x in (ob,ob1):
  x.msg()
  x.data()'''


#function based polymorphism
#method overriding
'''class A:
  def msg(self):
    print('Hello')
  def data(self):
    print('Rakesh')

class B:
  def msg(self):
    print('Hi')
  def data(self):
    print('sai')


def disp(ob):
  print('type: ',type(ob))
  ob.msg()
  ob.data()

if __name__=='__main__':
  ob=A()
  ob1=B()
  option = input('enter choice :')
  if option== 'A':
    disp(ob)
  elif option== 'B':
    disp(ob1)
  elif option== 'both':
    disp(ob)
    disp(ob1)
  else:
    print('invalid option')'''


'''#polymorphism with inheritance
class A:
  def msg(self):
    print('Hello')
  def data(self):
    print('Rakesh')

class B:
  def msg(self):
    print('Hi')
  def data(self):
    print('sai')

coll= [A() , B()]
for ob in coll:
  ob.msg()
  ob.data()'''

