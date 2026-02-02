#python lists

items= ["Bob", 10, True, 3.142]
print(items)
print(items[0])
print(items[3])
print(items[-3])
print(items[2:4])
items[1] = 25 #change second item
print(items)

fruits= ["orange", "watermelon", "mango", "guava", "banana"]
fruits[1] = "blueberry" #changes the second fruit to blueberry
print(fruits)

fruits.insert(2, "passion")
print(fruits[1])
fruits.pop(2)
fruits.remove("banana")
print(fruits)
