#python interface

'''python supports interface in 2 ways:
1. class with all MethodType
2.zope method'''

'''class ireposit_write:
  def newitem(self,data):
    pass
  def remove(self,data):
    pass
  def edit(self,ind,data):
    pass
class ireposit_read:
  def search(self,data):
    pass
  def dispall(self):
    pass

class transaction (ireposit_write,ireposit_read):
  def __init__(self):
    self.ds=[]
  def newitem(self,data):
    self.ds.append(data)
    print('item added')
  def remove(self,data):
    self.ds.remove(data)
    print('item removed')
  def edit(self,ind,item):
    self.ds[ind]=item
    print('item edited')
  def search(self,data):
    if data in self.ds:
      print('item found')
    else:
      print('item not found')
  def dispall(self):
    for x in self.ds:
      print(x)
if __name__=='__main__':
  t=transaction()
  t.newitem('a')
  t.newitem('b')
  t.newitem('c')
  t.dispall()
  t.remove('b')
  t.dispall()
  '''

'''class ireposit_write:
  def newitem(self, data):
      pass

  def remove(self, data):
      pass

  def edit(self, ind, data):
      pass


class ireposit_read:
  def search(self, data):
      pass

  def dispall(self):
      pass


class transaction(ireposit_write, ireposit_read):
  def __init__(self):
      self.ds = []

  def newitem(self, data):
      self.ds.append(data)
      print(f"Item '{data}' added")  # Added message for new item

  def remove(self, data):
      if data in self.ds:
          self.ds.remove(data)
          print(f"Item '{data}' removed")  # Added message for item removal
      else:
          print(f"Item '{data}' not found. Cannot remove.")

  def edit(self, ind, item):
      if 0 <= ind < len(self.ds):
          self.ds[ind] = item
          print(f"Item at index {ind} edited")  # Added message for item edit
      else:
          print("Invalid index. Cannot edit.")

  def search(self, data):
      if data in self.ds:
          print(f"Item '{data}' found")
      else:
          print(f"Item '{data}' not found")

  def dispall(self):
      print("All items:")
      for x in self.ds:
          print(x)


if __name__ == '__main__':
  t = transaction()
  t.newitem('a')
  t.newitem('b')
  t.newitem('c')
  t.dispall()

  t.remove('b')
  t.dispall()

  t.edit(1, 'd')
  t.dispall()'''

#zope interface
from zope.interface import Interface, implementer


class IRepoWrite(Interface):
    def newitem(self, data):
        pass

    def remove(self, data):
        pass

    def edit(self, ind, data):
        pass


class IRepoRead(Interface):
    def search(self, data):
        pass

    def dispall(self):
        pass


@implementer(IRepoWrite, IRepoRead)
class Transaction:
    def __init__(self):
        self.ds = []

    def newitem(self, data):
        self.ds.append(data)
        print(f"Item '{data}' added")

    def remove(self, data):
        if data in self.ds:
            self.ds.remove(data)
            print(f"Item '{data}' removed")
        else:
            print(f"Item '{data}' not found. Cannot remove.")

    def edit(self, ind, data):
        if 0 <= ind < len(self.ds):
            self.ds[ind] = data
            print(f"Item at index {ind} edited")
        else:
            print("Invalid index. Cannot edit.")

    def search(self, data):
        if data in self.ds:
            print(f"Item '{data}' found")
        else:
            print(f"Item '{data}' not found")

    def dispall(self):
        print("All items:")
        for x in self.ds:
            print(x)


if __name__ == '__main__':
    t = Transaction()
    t.newitem('a')
    t.newitem('b')
    t.newitem('c')
    t.dispall()

    t.remove('b')
    t.dispall()

    t.edit(1, 'd')
    t.dispall()
    t.search('d')

