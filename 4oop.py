# Encapsulation

class DataEngineer:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved +=1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    # def set_salary(self,value):
    #     self._salary = value

    def set_salary(self,base_value):
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self,base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

de = DataEngineer("Max",25)
# print(de.name,de.age)

for i in range(70):
    de.code()

de.set_salary(6000)         # Abstraction:=> It will hide the implementation of function, it only show simplex part
print(de.get_salary())