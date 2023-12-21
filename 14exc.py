'''import datetime
working=0
holiday=0
for x in range (1,30,1):
  do=datetime.datetime(2019,1,x)
  if (do.strftime("%A")=="Sunday") or (do.strftime("%A")=="Saturday"):
    holiday=holiday+1
  else:
    working=working+1
print ("Working days:",working)
print ("Holidays:",holiday)
wage=float(input('wage per day:'))
print ("Total wage:",wage*working)'''

'''import calendar

def last_dates_of_months(year):
    year = int(year)  # Convert the input year to an integer
    for month in range(1, 13):
        last_day = calendar.monthrange(year, month)[1]
        last_date = f"{last_day:02d}/{month:02d}/{year}"
        print(last_date)

for x in range(1, 13):
    year_input = input('Enter year: ')
    last_dates_of_months(year_input)
    break
'''

'''from datetime import datetime

def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def calculate_balance(principal, interest):
    balance = principal + interest
    return balance

print("Welcome to the Deposit Calculator!")

while True:
    # User inputs
    principal = float(input("Enter the deposit amount: $"))
    rate = float(input("Enter the interest rate (%): "))
    deposit_date = input("Enter the deposit date (YYYY-MM-DD): ")
    withdraw_date = input("Enter the withdrawal date (YYYY-MM-DD): ")

    # Calculating time in years between deposit and withdrawal
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(deposit_date, date_format)
    end_date = datetime.strptime(withdraw_date, date_format)
    time_delta = end_date - start_date
    time_in_years = time_delta.days / 365.25

    # Calculating interest
    interest = calculate_interest(principal, rate, time_in_years)

    # Calculating balance and total balance
    balance = calculate_balance(principal, interest)
    total_balance = principal + interest

    # Displaying options to the user
    print("\nChoose an option:")
    print("1. Find interest")
    print("2. Find balance")
    print("3. Find total balance")
    print("4. Exit")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        print(f"The interest on your deposit is: ${interest:.2f}")
    elif choice == 2:
        print(f"The current balance is: ${balance:.2f}")
    elif choice == 3:
        print(f"The total balance at the end is: ${total_balance:.2f}")
    elif choice == 4:
        print("Exiting the program. Thank you for using the Deposit Calculator!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")

# Add a final thank-you message outside the loop
print("Thank you for using the Deposit Calculator!")'''


'''from datetime import datetime

def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def calculate_balance(principal, interest):
    balance = principal + interest
    return balance

print("Welcome to the Deposit Calculator!")

# User inputs (outside the loop)
principal = float(input("Enter the deposit amount: $"))
rate = float(input("Enter the interest rate (%): "))
deposit_date = input("Enter the deposit date (YYYY-MM-DD): ")
withdraw_date = input("Enter the withdrawal date (YYYY-MM-DD): ")

while True:
    # Calculating time in years between deposit and withdrawal
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(deposit_date, date_format)
    end_date = datetime.strptime(withdraw_date, date_format)
    time_delta = end_date - start_date
    time_in_years = time_delta.days / 365.25

    # Calculating interest
    interest = calculate_interest(principal, rate, time_in_years)

    # Calculating balance and total balance
    balance = calculate_balance(principal, interest)
    total_balance = principal + interest

    # Displaying options to the user
    print("\nChoose an option:")
    print("1. Find interest")
    print("2. Find balance")
    print("3. Find total balance")
    print("4. Exit")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        print(f"The interest on your deposit is: ${interest:.2f}")
    elif choice == 2:
        print(f"The current balance is: ${balance:.2f}")
    elif choice == 3:
        print(f"The total balance at the end is: ${total_balance:.2f}")
    elif choice == 4:
        print("Exiting the program. Thank you for using the Deposit Calculator!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")'''


'''from datetime import datetime

def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def calculate_balance(principal, interest):
    balance = principal + interest
    return balance

print("Welcome to the Deposit Calculator!")

# User inputs
principal = float(input("Enter the deposit amount: $"))
rate = float(input("Enter the interest rate (%): "))
deposit_date = input("Enter the deposit date (YYYY-MM-DD): ")
withdraw_date = input("Enter the withdrawal date (YYYY-MM-DD): ")

while True:
    

    # Calculating time in years between deposit and withdrawal
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(deposit_date, date_format)
    end_date = datetime.strptime(withdraw_date, date_format)
    time_delta = end_date - start_date
    time_in_years = time_delta.days / 365.25

    # Calculating interest
    interest = calculate_interest(principal, rate, time_in_years)

    # Calculating balance and total balance
    balance = calculate_balance(principal, interest)
    total_balance = principal + interest

    # Displaying options to the user
    print("\nChoose an option:")
    print("1. Find interest")
    print("2. Find balance")
    print("3. Find total balance")
    print("4. Exit")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        print(f"The interest on your deposit is: ${interest:.2f}")
    elif choice == 2:
        print(f"The current balance is: ${balance:.2f}")
    elif choice == 3:
        print(f"The total balance at the end is: ${total_balance:.2f}")
    elif choice == 4:
        exit_choice = input("Do you want to exit the program? (yes/no): ").lower()
        if exit_choice == "yes":
            print("Exiting the program. Thank you for using the Deposit Calculator!")
            break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
'''

'''from datetime import datetime

def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def calculate_balance(principal, interest):
    balance = principal + interest
    return balance

print("Welcome to the Deposit Calculator!")

while True:
    # User inputs
    principal = float(input("Enter the deposit amount: $"))
    rate = float(input("Enter the interest rate (%): "))
    deposit_date = input("Enter the deposit date (YYYY-MM-DD): ")
    withdraw_date = input("Enter the withdrawal date (YYYY-MM-DD): ")

    # Calculating time in years between deposit and withdrawal
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(deposit_date, date_format)
    end_date = datetime.strptime(withdraw_date, date_format)
    time_delta = end_date - start_date
    time_in_years = time_delta.days / 365.25

    # Calculating interest
    interest = calculate_interest(principal, rate, time_in_years)

    # Calculating balance and total balance
    balance = calculate_balance(principal, interest)
    total_balance = principal + interest

    # Displaying options to the user
    print("\nChoose an option:")
    print("1. Find interest")
    print("2. Find balance")
    print("3. Find total balance")
    print("4. Exit")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        print(f"The interest on your deposit is: ${interest:.2f}")
    elif choice == 2:
        print(f"The current balance is: ${balance:.2f}")
    elif choice == 3:
        print(f"The total balance at the end is: ${total_balance:.2f}")
    elif choice == 4:
        print("Exiting the program. Thank you for using the Deposit Calculator!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")

    # Ask if the user wants to continue
    continue_option = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_option != 'yes':
        print("Exiting the program. Thank you for using the Deposit Calculator!")
        break
'''



'''from datetime import datetime

def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def calculate_balance(principal, interest):
    balance = principal + interest
    return balance

print("Welcome to the Deposit Calculator!")

while True:
    while True:
        try:
            # User inputs
            principal = float(input("Enter the deposit amount: Rs"))
            rate = float(input("Enter the interest rate (%): "))
            deposit_date = input("Enter the deposit date (YYYY-MM-DD): ")
            withdraw_date = input("Enter the withdrawal date (YYYY-MM-DD): ")

            # Check if dates are in the correct format
            date_format = "%Y-%m-%d"
            datetime.strptime(deposit_date, date_format)
            datetime.strptime(withdraw_date, date_format)

            break  # If all inputs are valid, break the input loop
        except ValueError:
            print("Invalid input. Please enter valid numerical values and dates in YYYY-MM-DD format.")

    # Calculating time in years between deposit and withdrawal
    start_date = datetime.strptime(deposit_date, date_format)
    end_date = datetime.strptime(withdraw_date, date_format)
    time_delta = end_date - start_date
    time_in_years = time_delta.days / 365.25

    # Calculating interest
    interest = calculate_interest(principal, rate, time_in_years)

    # Calculating balance and total balance
    balance = calculate_balance(principal, interest)
    total_balance = principal + interest

    # Displaying options to the user
    print("\nChoose an option:")
    print("1. Find interest")
    print("2. Find balance")
    print("3. Find total balance")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print(f"The interest on your deposit is: Rs{interest:.2f}")
    elif choice == '2':
        print(f"The current balance is: Rs{balance:.2f}")
    elif choice == '3':
        print(f"The total balance at the end is: Rs{total_balance:.2f}")
    elif choice == '4':
        print("Exiting the program. Thank you for using the Deposit Calculator!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")

    # Ask if the user wants to continue
    continue_option = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_option != 'yes':
        print("Exiting the program. Thank you for using the Deposit Calculator!")
        break
'''



#exception handling
#error can be handled using exception
'''try:
  x=int(input('enter no: '))
  print(x)
  print(type(x))
except:
  pass'''


'''try:
  x=int(input('enter no: '))
  print(x)
  print(type(x))
except:
  print('please enter numeric')'''


'''try:
  x=int(input('enter no: '))
  print(x)
  print(type(x))
  li=['a','b','c']
  print(li[10])
except ValueError as kc:print(kc)
except NameError as kc1:print('no such variable declared')
except IndexError as kc2:print('index error')  
else:
  print('no error')
finally:
  print('finally')
  '''

''''. ZeroDivisionError Handling
Write a program that handles a ZeroDivisionError when dividing a number by zero.

python
Copy code
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
2. ValueError Handling
Handle a ValueError when trying to convert a string to an integer.

python
Copy code
try:
    num = int("hello")
except ValueError as e:
    print("Error:", e)
3. IndexError Handling
Handle an IndexError when accessing an index that is out of range in a list.

python
Copy code
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print("Error:", e)
4. KeyError Handling
Handle a KeyError when accessing a non-existent key in a dictionary.

python
Copy code
my_dict = {'a': 1, 'b': 2}
try:
    print(my_dict['c'])
except KeyError as e:
    print("Error:", e)
5. FileNotFoundError Handling
Handle a FileNotFoundError when trying to open a file that doesn't exist.

python
Copy code
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print("Error:", e)
6. TypeError Handling
Handle a TypeError when trying to concatenate incompatible types.

python
Copy code
try:
    result = "hello" + 10
except TypeError as e:
    print("Error:", e)
7. AssertionError Handling
Handle an AssertionError by raising and catching it.

python
Copy code
try:
    x = 10
    assert x < 5, "x should be less than 5"
except AssertionError as e:
    print("Error:", e)
8. Custom Exception Handling
Create and handle a custom exception in a function.

python
Copy code
class CustomError(Exception):
    pass

def func(value):
    try:
        if value < 0:
            raise CustomError("Value should be positive")
    except CustomError as e:
        print("Error:", e)

func(-5)
9. Using else with try-except
Implement an else block that runs if no exception occurs.

python
Copy code
try:
    num = int(input("Enter a number: "))
except ValueError as e:
    print("Error:", e)
else:
    print("You entered:", num)
10. Using finally with try-except
Implement a finally block to perform cleanup operations.

python
Copy code
try:
    file = open('sample.txt', 'r')
    # Perform file operations
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()
11. Handling Multiple Exceptions
Handle multiple exceptions in a single try-except block.

python
Copy code
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError) as e:
    print("Error:", e)
12. Nested Exception Handling
Implement nested exception handling to catch specific exceptions.

python
Copy code
try:
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise ValueError("Division error occurred") from e
except ValueError as e:
    print("Error:", e)
13. Raising Exceptions
Raise an exception explicitly.

python
Copy code
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)
14. Handling KeyboardInterrupt
Handle a KeyboardInterrupt exception.


try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
  
15. Handling RecursionError
Create a function that triggers a RecursionError.


def recursive_func():
    return recursive_func()

try:
    recursive_func()
except RecursionError as e:
    print("Error:", e)


16. Handling MemoryError
Simulate a MemoryError.


try:
    my_list = [0] * 10**8  # Creating a huge list
except MemoryError as e:
    print("Error:", e)


17. Handling StopIteration
Handle a StopIteration exception.


my_iter = iter([1, 2, 3])
try:
    while True:
        print(next(my_iter))
except StopIteration:
    print("End of iterator")


18. Handling FloatingPointError
Simulate a FloatingPointError.

try:
    result = 10.0 ** 1000
except OverflowError as e:
    print("Error:", e)


19. Handling AttributeError
Handle an AttributeError when accessing a non-existent attribute.
  
class MyClass:
    pass

obj = MyClass()
try:
    print(obj.attribute)
except AttributeError as e:
    print("Error:", e)


20. Handling ImportErrors
Handle an ImportError when importing a non-existent module.

try:
    import non_existent_module
except ImportError as e:
    print("Error:", e)'''

#type error
'''import math


def disp(x):
  if isinstance(x,int) or isinstance(x,float):
    print(math.pow(x,2))
  else:
    raise TypeError ('please enter only numeric data')

if __name__=='__main__':
  try:
    disp('a')
  except TypeError as e: 
    print(e)
  finally:
    print('over')'''


'''class CustomError(Exception):
    def __init__(self, message="This is a custom exception"):
        self.message = message
        super().__init__(self.message)

# Example usage:
def divide(a, b):
    if b == 0:
        raise CustomError("Division by zero is not allowed")
    return a / b

# Handling the custom exception:
try:
    result = divide(10, 0)
    print("Result:", result)
except CustomError as e:
    print("Error:", e)
'''

'''class kc_exception(Exception):
    def __init__(self,msg):
        self.err=msg
    def __str__(self)    :
        return self.err
class SBI_tran:
    def new_account(self,amount):
        if (amount<=5000) :
            raise kc_exception("account creation failed , min amount exceeded")
        else :
            print(amount)
    def new_account1(self,dt):
        if dt.strftime('%A')== 'Saturday' or dt.strftime('%A')== 'Sunday':
            raise kc_exception("account creation failed , holidays")
        else:
            print('txn over')
if __name__=='__main__':
    try :
        ob=SBI_tran()
        ob.new_account(34000)
        print("account created successfully")
    except kc_exception as kc:
        print(kc)
    except Exception as rk:
        print(rk)
    else:
        print('okay')
    finally:
        print('no transaction')'''
