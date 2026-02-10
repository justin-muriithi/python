#grading system
subject1=int(input("enter marks1:"))
subject2=int(input("enter marks2:"))
subject3=int(input("enter marks3:"))
average=(subject1+subject2+subject3)/3
print("average:", average)

if (average>=70):
    grade="A"
elif (average>=60 and average<=69):
    grade="B"
elif(average>=50 and average<=59):
    grade="C"
elif(average>=40 and average<=49):
    grade="D"
else:
    grade="fail"

print("grade:", grade)
