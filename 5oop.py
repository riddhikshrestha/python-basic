# Properties

class DataEngineer:

    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        # check, constraints, calcualtions
        return self._salary

    @salary.setter
    def salary(self,value):
        self._salary = value

    # @salary.deleter
    # def salary(self):
    #     del self._salary

de = DataEngineer()
# print(de.name,de.age)


de.salary = 7000      
print(de.salary)
# del de.salary
# print(de.salary)