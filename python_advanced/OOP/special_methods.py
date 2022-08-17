"""
    - Topic : __str__
    - Description : to customize what will print() function print
    - Source Link : https://www.pythontutorial.net/python-oop/python-__str__/
"""
#%%


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """to customize what will print() function print"""
        return f"Person({self.first_name}, {self.last_name}, {self.age})"


# %%
person = Person(first_name="John", last_name="Doe", age=18)
print(person)

#%%
"""
    - Topic : __repr__
    - Description : __str__ is for human-readable, __repr__ is for machine-readable
    - Source Link : https://www.pythontutorial.net/python-oop/python-__repr__/
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        """to customize the string representation for machine-readable"""
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        """to customize the string representation for human-readable"""
        return f"({self.first_name},{self.last_name},{self.age})"


#%%
person = Person("John", "Doe", 25)
# use str()
print(person)

# use repr()
print(repr(person))

# %%
"""
    - Topic : __eq__
    - Description : to comparing objects by values
    - Source Link : https://www.pythontutorial.net/python-oop/python-__eq__/
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        """to do comparizon between sepcific attributes"""
        if isinstance(other, Person):
            return self.age == other.age
        return False


#%%
john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)
print(john == jane)  # True

mary = Person("Mary", "Doe", 27)
print(john == mary)  # False

print(john == 20)

# %%
"""
    - Topic : __hash__
    - Description : to make a class hashable
    - Source Link : https://www.pythontutorial.net/python-oop/python-__hash__/
"""

# The hash() function accepts an object and returns the hash value as an integer
print(hash(john))  # TypeError: unhashable type: 'Person'
# If a class overrides the __eq__ method, the object of the class become "unhashable", the __hash__ is set to None

#%%


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        """make class hashable"""
        return hash(self.age)


#%%
john = Person(name="John", age=18)
print(hash(john))

#%%
# Since using age to hash, the hash of the class should remain immutable
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def __eq__(self, other) -> bool:
        return isinstance(other, Person) and self._age == other._age

    def __hash__(self) -> int:
        return hash(self._age)


#%%
p1 = Person("Paul", 18)
print(hash(p1))
print(p1 == 20)
print(p1 == john)

# %%
"""
    - Topic : __bool__
    - Description : determine whether a custom object is True/False
    - Source Link : https://www.pythontutorial.net/python-oop/python-__bool__/
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True


#%%
person = Person("Jane", 16)
print(bool(person))  # False

#%%

"""
    Some rules for __bool__
    - If a custom class doesn’t have the __bool__ method, Python will look for the __len__() method.
    - If a class doesn’t implement the __bool__ and __len__ methods, the objects of the class will evaluate to True.

"""


class Payroll:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        print("len was called...")
        return self.length


#%%
payroll = Payroll(0)
print(bool(payroll))  # False

payroll.length = 10
print(bool(payroll))  # True

# %%
"""
    - Topic : __del__
    - Description : to delete attributes
    - Source Link : https://www.pythontutorial.net/python-oop/python-__del__/
"""
"""
    Some rules for __del__
    - When we set the object to `None` or `del` it, the garbage collector destroys it because there's no reference, and the __del__ is called.
    - __del__ method didn't destroys the object, the garbage collector did.
    - Should not use the __del__ method to clean up the resources. It’s recommended to use the context manager.
    - If an exception occurs inside the __del__ method, Python does not raise the exception but keeps it silent.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("__del__ was called")


# %%
person = Person("John Doe", 23)
person = None

# %%
person = Person("John Doe", 23)
del person
# %%
