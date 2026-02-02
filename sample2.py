#program 
a = 10
b = 20.3
sum = a+b
fname = "John"
tall = True

print(sum) #30.3
print("the sum is",sum)
print("Name is" + fname + "and sum is" + str(sum))
print(f"the sum is {sum:.2f} and name is {fname}")

#python files:create/open, write, close
f=open("C:\\Users\\user\\OneDrive\\Documents\\python\\sample.txt", "w") #
print("this is a sample text", file=f)
print(f"the sum is {sum:.2f} and name is {fname}"),
print(a,b,sum,file=f)
f.close()

last_name = input("Enter your Name:")
score = int(input("Enter marks"))
budget = float(input("Enter budget:"))

#user screen
print(" last_name: ",last_name)
print(" score: ",score)
print(" budget: ",budget)

#displaying on a file
f=open("C:\\Users\\user\\OneDrive\\Documents\\python\\sample.txt", "a")
print("last_name: ",last_name, file=f)
print("score: ",score, file=f)
print("budget: ",budget, file=f)
f.close()

