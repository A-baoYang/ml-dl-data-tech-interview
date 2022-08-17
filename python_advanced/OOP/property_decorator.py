"""
    - Topic : @property decorator
    - Description : Use @property decorator to define property for a class
    - Source link : https://www.pythontutorial.net/python-oop/python-property-decorator/
"""
#%%


class Person:
    def __init__(self, name, age):
        self.name = name
        self.init_age = age

    """ Use @property to decorate init_age() method and simplify the property definition from using property() """

    @property
    def init_age(self):
        return self._age

    """ Call the setter() method of the init_age property object """
    """ Use the decorator @init_age.setter for the set_age() method """

    @init_age.setter
    def init_age(self, value):
        if value <= 0:
            raise ValueError("Age must be positive")
        self._age = value

    # The property() accepts a callable (age) and returns a callable. Therefore, it is a decorator.


# %%

p1 = Person("Joe", -1)  # ValueError: Age must be positive
# %%

p1 = Person("Joe", 18)
p1.init_age  # 18
p1.name  # Joe

#%%
# Sample Code
class MyClass:
    def __init__(self, attr_a, attr_b):
        self.prop_a = attr_a
        self.prop_b = attr_b

    @property
    def prop_a(self):
        return self.__attr_a

    @prop_a.setter
    def prop_a(self, value):
        self.__attr_a = value

    @property
    def prop_b(self):
        return self.__attr_b

    @prop_b.setter
    def prop_b(self, value):
        self.__attr_b = value
