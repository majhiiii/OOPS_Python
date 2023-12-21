#operator overloading: same operator performing differently on different objects

'''x=10
y=20
z=x+y
print(z)

x='a'
y='b'
z=x+y
print(z)

x=10
y=20
z=x*y
print(z)

x='rakesh '
result = x*4
li= [result]
print(li)'''

'''class kc_operator:
  def __init__(self,a):
    self.a=a

ob=kc_operator(10)
ob1=kc_operator(20)
ob3=ob.a+ob1.a
print(ob3)'''
#ob=kc_operator(10)
#ob1=kc_operator(20)
#ob3=kc_operator(None)
#ob3.a=ob.a+ob1.a
#print(ob3.a)


'''class kc_operator:
  def __init__(self,a):
    self.a=a
  def __add__(self,other):
    return self.a+other.a
ob=kc_operator(10)
ob1=kc_operator(20)
ob3=ob+ob1
print(ob3)'''
'''
class Number:
  def __init__(self, value):
      self.value = value

  def __neg__(self):
      return Number(-self.value)

  def __pos__(self):
      return Number(self.value)

  def __invert__(self):
      return Number(~self.value)

  def __str__(self):
      return str(self.value)

# Creating an instance of the Number class
num = Number(10)

# Unary operator overloading
neg_num = -num
pos_num = +num
inv_num = ~num

# Displaying the results
print(f"Original Number: {num}")   # Output: Original Number: 10
print(f"Negative Number: {neg_num}")  # Output: Negative Number: -10
print(f"Positive Number: {pos_num}")  # Output: Positive Number: 10
print(f"Inverted Number: {inv_num}")  # Output: Inverted Number: -11

'''
'''class abacus_:
  def __init__(self,a):
    self.a=a
  def __add__(self,b):
    return self.a+b.a

ob=abacus_(10)
ob1=abacus_(20)
result=ob+ob1
print(result)'''


'''class abacus_:
  def __init__(self,a):
    self.a=a
  def __sub__(self,b):
    return self.a-b.a

ob=abacus_(10)
ob1=abacus_(20)
result=ob-ob1
print(result)'''


class Number:
  def __init__(self, value):
      self.value = value

  def __isub__(self, other):
      self.value -= other.value
      return self  # Returning self allows for method chaining

# Creating instances of the Number class
num1 = Number(20)
num2 = Number(10)

# Performing in-place subtraction using '-=' operator
num1 -= num2

print(num1.value)  # Output: 10 (20 - 10 = 10)



