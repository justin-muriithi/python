#decision making
name = input("Enter name:")
salary= float(input("Enter salary:"))
year= int(input("Enter years of service:"))
if (year>10):
    bonus= 0.1 * salary
elif (year >=6 and year <=10):
    bonus= 0.8 * salary
else:
    bonus= 0.6 * salary

print("the bonus is", bonus)
f=open("C:\\Users\\user\\OneDrive\\Documents\\python\\decisionmaking.py.txt", "w")
print("The bonus is:", bonus, file=f)
f.close()
