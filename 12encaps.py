'''# Python program to 
# demonstrate protected members 

# Creating a base class 
class Base: 
  def __init__(self): 

    # Protected member 
    self._a = 2

# Creating a derived class 
class Derived(Base): 
  def __init__(self): 

    # Calling constructor of 
    # Base class 
    Base.__init__(self) 
    print("Calling protected member of base class: ", 
      self._a) 

    # Modify the protected variable: 
    self._a = 3
    print("Calling modified protected member outside class: ", 
      self._a) 


obj1 = Derived() 

obj2 = Base() 

# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected member of obj1: ", obj1._a) 

# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2._a) 

#PRIVATE MEMBERS
# Python program to 
# demonstrate private members 

# Creating a Base class 


class Base: 
  def __init__(self): 
    self.a = "GeeksforGeeks"
    self.__c = "GeeksforGeeks"

# Creating a derived class 
class Derived(Base): 
  def __init__(self): 

    # Calling constructor of 
    # Base class 
    Base.__init__(self) 
    print("Calling private member of base class: ") 
    print(self.__c) 


# Driver code 
obj1 = Base() 
print(obj1.a) 

# Uncommenting print(obj1.c) will 
# raise an AttributeError 

# Uncommenting obj2 = Derived() will 
# also raise an AttributeError as 
# private member of base class 
# is called inside derived class 


'''
'''
class Employee:
  def __init__(self, emp_id, name, position, department):
      self.emp_id = emp_id
      self.name = name
      self.position = position
      self.department = department

class EmployeeManagementSystem:
  def __init__(self):
      self.employees = []
      self.departments = set()

  def create_employee(self):
      emp_id = input("Enter employee ID: ")
      name = input("Enter employee name: ")
      position = input("Enter employee position: ")
      department = input("Enter employee department: ")
      self.departments.add(department)
      employee = Employee(emp_id, name, position, department)
      self.employees.append(employee)
      print("Employee created successfully!")

  def display_employees(self):
      if not self.employees:
          print("No employees found.")
      else:
          print("Employee List:")
          for employee in self.employees:
              print(f"ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}, Department: {employee.department}")

  def update_employee(self):
      emp_id = input("Enter employee ID to update: ")
      for employee in self.employees:
          if employee.emp_id == emp_id:
              name = input("Enter updated name: ")
              position = input("Enter updated position: ")
              department = input("Enter updated department: ")
              self.departments.add(department)
              employee.name = name
              employee.position = position
              employee.department = department
              print("Employee details updated successfully!")
              return
      print("Employee ID not found.")

  def delete_employee(self):
      emp_id = input("Enter employee ID to delete: ")
      for employee in self.employees:
          if employee.emp_id == emp_id:
              self.employees.remove(employee)
              print("Employee deleted successfully!")
              return
      print("Employee ID not found.")

  def print_all_employee_data(self):
      if not self.employees:
          print("No employees found.")
      else:
          print("All Employee Details:")
          for employee in self.employees:
              print(f"ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}, Department: {employee.department}")

  def create_department(self):
      department = input("Enter new department name: ")
      self.departments.add(department)
      print("New department added successfully!")

  def display_departments(self):
      if not self.departments:
          print("No departments found.")
      else:
          print("Departments List:")
          for department in self.departments:
              print(f"- {department}")

  def update_department(self):
      if not self.departments:
          print("No departments found to update.")
          return

      old_department = input("Enter department name to update: ")
      if old_department in self.departments:
          new_department = input("Enter updated department name: ")
          self.departments.remove(old_department)
          self.departments.add(new_department)
          print("Department updated successfully!")
      else:
          print("Department not found.")

  def delete_department(self):
      if not self.departments:
          print("No departments found to delete.")
          return

      department = input("Enter department name to delete: ")
      if department in self.departments:
          self.departments.remove(department)
          print("Department deleted successfully!")
      else:
          print("Department not found.")

  def search_and_add_employee(self):
      search_value = input("Enter employee ID or name to search: ")
      found = False
      for employee in self.employees:
          if search_value.lower() in employee.emp_id.lower() or search_value.lower() in employee.name.lower():
              print(f"Employee found! ID: {employee.emp_id}, Name: {employee.name}")
              found = True
              break
      if not found:
          print("Employee not found. Adding new employee...")
          self.create_employee()

def main():
  emp_sys = EmployeeManagementSystem()

  while True:
      print("\nEmployee Management System Menu:")
      print("1. Create Employee")
      print("2. Display Employees")
      print("3. Update Employee")
      print("4. Delete Employee")
      print("5. Print All Employee Data")
      print("6. Add Department")
      print("7. Display Departments")
      print("8. Update Department")
      print("9. Delete Department")
      print("10. Search and Add Employee")
      print("11. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
          emp_sys.create_employee()
      elif choice == "2":
          emp_sys.display_employees()
      elif choice == "3":
          emp_sys.update_employee()
      elif choice == "4":
          emp_sys.delete_employee()
      elif choice == "5":
          emp_sys.print_all_employee_data()
      elif choice == "6":
          emp_sys.create_department()
      elif choice == "7":
          emp_sys.display_departments()
      elif choice == "8":
          emp_sys.update_department()
      elif choice == "9":
          emp_sys.delete_department()
      elif choice == "10":
          emp_sys.search_and_add_employee()
      elif choice == "11":
          print("Exiting the Employee Management System.")
          break
      else:
          print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
  main()
'''








'''class Employee:
  def __init__(self, emp_id, name, position, department):
      self.emp_id = emp_id
      self.name = name
      self.position = position
      self.department = department

class EmployeeManagementSystem:
  def __init__(self):
      self.employees = []
      self.departments = set()

  def create_employee(self):
      emp_id = input("Enter employee ID: ")
      name = input("Enter employee name: ")
      position = input("Enter employee position: ")
      department = input("Enter employee department: ")
      self.departments.add(department)
      employee = Employee(emp_id, name, position, department)
      self.employees.append(employee)
      print("Employee created successfully!")

  def display_employees(self):
      if not self.employees:
          print("No employees found.")
      else:
          print("\nEmployee List:")
          print("{:<15} {:<20} {:<20} {:<15}".format("Employee ID", "Name", "Position", "Department"))
          print("-" * 70)
          for employee in self.employees:
              print("{:<15} {:<20} {:<20} {:<15}".format(employee.emp_id, employee.name, employee.position, employee.department))
          print("-" * 70)

  def update_employee(self):
      emp_id = input("Enter employee ID to update: ")
      for employee in self.employees:
          if employee.emp_id == emp_id:
              name = input("Enter updated name: ")
              position = input("Enter updated position: ")
              department = input("Enter updated department: ")
              self.departments.add(department)
              employee.name = name
              employee.position = position
              employee.department = department
              print("Employee details updated successfully!")
              return
      print("Employee ID not found.")

  def delete_employee(self):
      emp_id = input("Enter employee ID to delete: ")
      for employee in self.employees:
          if employee.emp_id == emp_id:
              self.employees.remove(employee)
              print("Employee deleted successfully!")
              return
      print("Employee ID not found.")

  def print_all_employee_data(self):
      if not self.employees:
          print("No employees found.")
      else:
          print("\nAll Employee Details:")
          print("{:<15} {:<20} {:<20} {:<15}".format("Employee ID", "Name", "Position", "Department"))
          print("-" * 70)
          for employee in self.employees:
              print("{:<15} {:<20} {:<20} {:<15}".format(employee.emp_id, employee.name, employee.position, employee.department))
          print("-" * 70)

  def display_employees_by_department(self):
      if not self.employees:
          print("No employees found.")
      else:
          departments_employees = {}
          for employee in self.employees:
              if employee.department not in departments_employees:
                  departments_employees[employee.department] = []
              departments_employees[employee.department].append(employee)

          print("\nEmployees by Department:")
          for department, employees in departments_employees.items():
              print(f"\nDepartment: {department}")
              print("{:<15} {:<20} {:<20}".format("Employee ID", "Name", "Position"))
              print("-" * 55)
              for employee in employees:
                  print("{:<15} {:<20} {:<20}".format(employee.emp_id, employee.name, employee.position))
              print("-" * 55)


def main():
  emp_sys = EmployeeManagementSystem()

  while True:
      print("\nEmployee Management System Menu:")
      print("1. Create Employee")
      print("2. Display Employees")
      print("3. Update Employee")
      print("4. Delete Employee")
      print("5. Print All Employee Data")
      print("6. Display Employees by Department")
      print("7. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
          emp_sys.create_employee()
      elif choice == "2":
          emp_sys.display_employees()
      elif choice == "3":
          emp_sys.update_employee()
      elif choice == "4":
          emp_sys.delete_employee()
      elif choice == "5":
          emp_sys.print_all_employee_data()
      elif choice == "6":
          emp_sys.display_employees_by_department()
      elif choice == "7":
          print("Exiting the Employee Management System.")
          break
      else:
          print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
  main()
'''

'''
from random import randint

class Bank:
    def __init__(self) -> None:
        self.name= input("enter name :")
        self.__account_no= randint(1000,555555)
        self.__balance= 0
    def dsiplayBalance(self): #getter
        print(f"your balance is {self.__balance}")

    def setBalance(self,Newbalance):  #setter
        self.__balance= Newbalance
        
    def display(self):
        print(f"name : {self.name}")
        print(f"account no : {self.__account_no}")
        print(f"balance : {self.__balance}")

obj=Bank()
obj.display()
obj.dsiplayBalance()
obj.setBalance(122424)
obj.display()

        '''

'''
class father:
    def __init__(self) -> None:
        self.father_name=input('enter fathers name :')
        self._bank_balance= int(input('enter balance:'))  #protected
        self.__phone_model= input('enter phone model=')   #private
    def displayfather(self):
        print(f'father name : {self.father_name}')
        print(f'balance : {self._bank_balance}')
        print(f'phone model : {self.__phone_model}')
    
class Child(father):
    def __init__(self) -> None:
        super().__init__()
        self.child_name=input('enter child name:')

    def displaychildinfo(self):
        print(f'child name : {self.child_name}')
        print(f'balance : {self._bank_balance}')
       # print(f'phone model : {self.__phone_model}')


child= Child()
child.displaychildinfo()'''


'''
class Animal:
    def sound(self):
        print('animal speaking')

class dog(Animal):
    def sound(self):
        print('bhaw bhaw')

class cat(Animal):
    def sound(self):
        print('meow meow')


obj= dog()
obj.sound()'''

#dunder methods only in python to directly print object

class father:
    def __init__(self) -> None:
        self.father_name=input('enter fathers name :')
        self._bank_balance= int(input('enter balance:'))  #protected
        self.__phone_model= input('enter phone model=')   #private

    def __str__(self) -> str: 
        return f'father name : {self.father_name}'
        
    def displayfather(self):
        print(f'father name : {self.father_name}')
        print(f'balance : {self._bank_balance}')
        print(f'phone model : {self.__phone_model}')


obj= father()
print('---------------')
obj.displayfather()
print('---------------')
print(obj)