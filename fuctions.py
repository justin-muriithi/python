#python functions
#user defined functions
""""def myName():
    print("My name is Justin")
#function call
myName()"""


"""def sum(a,b):
    sum = a + b
    return sum
#function call
print(sum(10,20))"""


"""def myName (name,age):
    
    print(f"My name is "+name+" and Iam "+str(age)+"years old")
    

name= (input("Enter your name:"))
age= int(input("Enter your age:"))
myName(name,age)"""


"""#simple interest
def simple_interest (principle,rate,time):
    
    

principle=int(input("enter principle:"))
rate=float(input("enter rate:"))
time=int(input("enter time:"))
simple_interest=principle*rate/100*time

print("simple_interest is principle*rate/100*time")
simple_interest(principle,rate,time)"""

#volume of a cylinder
import math
radius=int(input("enter radius:"))
height=int(input("enter height:"))

def volume(radius,height):
    volume=math.pi*math.pow(radius,2)*height
    return volume
print(volume(radius,height))
    
