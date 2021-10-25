# Functions in class
# Class
class DataScienceEngineer:
    
    #class attributes
    position = "Data Science"

    def __init__(self,name,age,level,salary):
        # instance attributes  => It only belongs to one object we create
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code..")

    def code_in_language(self,language):
        print(f"{self.name} is writing in {language}..")
    
    # def information(self):
        # information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        # return information

    # Special or dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self,other):
        return self.name == other.name and self.age == other.age 

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

# Instance
de1 = DataScienceEngineer("Prem",28,"Senior",75000)
de2 = DataScienceEngineer("Ud",27,"Mid",30000)
de3 = DataScienceEngineer("Ud",27,"Mid",30000)

de1.code()

de1.code_in_language("Python")

# print(de1.information())

print(de1)
print(de2)
print(de2 == de3)

print(de1.entry_salary(27))
print(DataScienceEngineer.entry_salary(23))

