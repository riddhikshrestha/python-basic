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

# Instance
de1 = DataScienceEngineer("Prem",28,"Senior",75000)
print(de1.name, de1.age)
print(DataScienceEngineer.position)
print(de1.position)

"""
# Inheritance
--------------
Inheritance is the process by which one clas takes on the attributes and methods of another.
Newly formed classes are called child class, and the classes that child classes are derived from are called parent classes.

Child classes inherit all of the parent's attributes and methods but also extend and overrides attributes and methods that are unique to themselves.

# Polymorphism
--------------
"Many Forms"

We can write a code that works on the superclass, and it will work with any subclass type as well.

Gives a way to use a class exactly like its parent, but each child keeps its own method as they are.


# Encapsulation
---------------
Encapsulation is the mechanism of hidding of data implementation.

Instance variable are keep private and accessor methods are made public to achieve this. With this, we restrict access to public methods (getter/setter).

Instance methods can also kept private.

# Abstraction
--------------
Abstraction can be thought of as a natural extension of encapsulation.
Applying abstraction means that each object should only expose a high-level mechanism for using it.

This mechanism should hide internal implementation details.
It should only revel or show operations relevent for the other objects.

"""