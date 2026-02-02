#hello world program
print("Hello World")
#program 
a = 10
b = 20.3
sum = a+b
name = "John"
tall = True

print(sum) #30.3
print("the sum is",sum)
print("Name is" + name + "and sum is" + str(sum))
print(f"the sum is {sum:.2f} and name is {name}")

#python files:create/open, write, close
f=("C:\\Users\\user\\OneDrive\\Documents\\python\\sample.txt", "w") #
print("this is a sample text", file=f)
print(f"the sum is {sum:.2f} and name is {name}"),
print(a,b,sum,file=f)
f.close()
      
