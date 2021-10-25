# INHERITANCE
# It is the process in which one class take attributes and method of other class
# It is called parent- child relationship

# inherits, extend, override
class Employee:
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working..")

class DataEngineer(Employee):
    def __init__(self,name,age,salary,level):
        super().__init__(name,age,salary)
        self.level = level
    
    def work(self):
        print(f"{self.name} is coding..")

    def debug(self):
        print(f"{self.name} is debugging..")

class Designer(Employee):

    def work(self):
        print(f"{self.name} is desiging..")

    def draw(self):
        print(f"{self.name} is drawing..")


de = DataEngineer("Maxi",26,40000,"Senior")
# de.work()


design = Designer("Chrish",20,30000)

# design.work()


# Polymorphishm

employees = [DataEngineer("Max",25,6000,"Junior"),
            DataEngineer("Lisa",30,9000,"Senior"),
            Designer("Philip",27,7000)]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)