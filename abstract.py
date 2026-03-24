from abc import ABC, abstractmethod
class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def display_info(self):
        print(f"Name: {self.__name}")

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.__salary()
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return self.__salary()/2

    
