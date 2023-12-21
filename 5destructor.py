#destructor


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
  def __del__(self):
    print('collection destroyed')
    del self.ds
  
ob=Kc_class()
ob.additem(emp(1,'rakesh','delhi'))
ob.additem(emp(2,'ankit','bbsr'))
ob.additem(emp(3,'hari','bbsr'))
ob.disp()
del ob