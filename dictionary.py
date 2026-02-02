#dictionaries
student= {
    "name":"Justin",
    "reg_no":"BSCIT-05-0071/2024",
    "DOB":"2005"
    }
print(student)
print(student.keys())
print(student.values())
print(student.items())
student.update({"email":"justinmuriithi831@gmail.com"})
print(student)
student.get("name")
