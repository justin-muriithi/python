#basic syntax
#try:

#except Exceptiontype:


#example:handling division b zero

#try:
   # result = 10/0
#except ZeroDivisionError:
    #print(f"cannot divide by zero!")


try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")

#handling different errors separately
try:
     num = int(input("enter a number:"))
     result = 10 / num
except ValueError:
     print("Invalid input! please input a number.")
except ZeroDivisionEror:
     print("cannot divide by zero!")
else:
     print("result:", result)
finally:
     print("successfully executed")

#raising exceptions manually
def withdraw(amount):
    if amount < 0:
        raise ValueError("amount cannot be negative")
    print(f"Withdrawn {amount}")

try:
    withdrawn(500, 100)
except NegativeBalanceError as e:
    print(f"transaction failed {e}")
    
