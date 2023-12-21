#overloading

'''#predefined
li=[1,2,3,4,5,6,7,8,9,10]
s='abacus'
print(li)
print(s)
print(len(li))
print(len(s))'''

#userdefined

'''def disp(dtype,*args):
  if dtype=='int':
    res=0
  elif dtype=='str':
    res=''
  elif dtype=='float':
    res=0.0
  for x in args:
    res+=x
  print(res)

if __name__=='__main__':
  disp('int',1,2,3,4,5,6,7,8,9,10)
  disp('str','a','b','c','u','s')
  disp('float',1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.10)'''



'''def disp(dtype,*args):
  if dtype==int:
    res=0
  elif dtype==str:
    res=''
  elif dtype==float:
    res=0.0
  for x in args:
    res+=x
  print(res)

if __name__=='__main__':
  disp(int,1,2,3,4,5,6,7,8,9,10)
  disp(str,'a','b','c','u','s')
  disp(float,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.10)'''

'''class rk_overloading:
  def disp(self,dtype,*args):
    if dtype=='int':
      self.res=0
    elif dtype=='str':
      self.res=''
    elif dtype=='float':
      self.res=0.0
    for x in args:
      self.res+=x
    print(self.res)

if __name__=='__main__':
  ob=rk_overloading()
  ob.disp('int',1,2,3,4,5,6,7,8,9,10)
  ob.disp('str','a','b','c','u','s')
  ob.disp('float',1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.10)'''


'''def disp(x,y):
  if isinstance(x,int) ==True and isinstance(y,int)==True:
    print('int')
    print(x+y)
  elif isinstance(x,float)==True and isinstance(y,float)==True:
    print('float')
    print(x+y) 

disp(10,20)
disp(10.2,20.5)'''

'''def disp(x, y):
  if isinstance(x, int) and isinstance(y, int):
      return int(x + y)
  elif isinstance(x, float) and isinstance(y, float):
      return float(x + y)
  else:
      return "Unsupported types or mixed types."

result1 = disp(10, 20)
result2 = disp(10.2, 20.5)
result3 = disp(10, 20.5)  

print(result1)  # Output: 30 (int)
print(result2)  # Output: 30.7 (float)
print(result3)  # Output: Unsupported types or mixed types.'''

'''from multimethod import multimethod
@multimethod
def disp(x:int,y:int):
  return(x+y)

@multimethod
def disp(x:float,y:float):
  return(x+y)

@multimethod
def disp(x:str,y:str):
  return(x+y)

if __name__=='__main__':
  print(disp(10,20))
  print(disp(10.2,20.5))
  print(disp('a','b'))'''



'''from multimethod import multimethod
class rk_overloading:
  @multimethod
  def disp(self,x:int,y:int):
    return(x+y)
  
  @multimethod
  def disp(self,x:float,y:float):
    return(x+y)
  
  @multimethod
  def disp(self,x:str,y:str):
    return(x+y)

if __name__=='__main__':
  ob=rk_overloading()
  print(ob.disp(10,20))
  print(ob.disp(10.2,20.5))
  print(ob.disp('a','b'))'''

#multiple dispatch overload method:

'''from multipledispatch import dispatch
@dispatch(int,int)
def disp(x,y):
  print(x,y)

@dispatch(str)
def disp(x):
  print(x)

@dispatch(int,str,bool)
def disp(x,y,z):
  print(x,y,z)

disp(10,20)
disp('a')
disp(10,'rakesh',True)'''


from multipledispatch import dispatch
class overloads:
  @dispatch(int,int)
  def disp(x,y):
    print(x,y)
  
  @dispatch(str)
  def disp(x):
    print(x)
  
  @dispatch(int,str,bool)
  def disp(x,y,z):
    print(x,y,z)
if __name__=='__main__':
  ob=overloads()
  ob.disp(10,20)
  ob.disp('a')
  ob.disp(10,'rakesh',True)

