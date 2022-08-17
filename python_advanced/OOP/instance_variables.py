"""
    - Topic : Instance Variable
    - Source Links : https://www.pythontutorial.net/python-oop/python-__init__/, https://www.pythontutorial.net/python-oop/python-instance-variables/
"""
#%%
"""
    __init__()
    - double underscores init, "dunder init"
    - Python will use the method internally
    - Python will automatically call the __init__() method immediately after creating a new object
    - use to initialize the object's attributes
"""


class Person:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age


#%%
person = Person("John")
print(f"I'm {person.name}. I'm {person.age} years old.")

# %%

"""
    Class variables:
    - bound to a class

    Instance variables: (instance attributes)
    - bound to a specific instance of a class
    - stored in the __dict__ attibute of the instance
    - Python find variables order: from __dict__ of the instance -> from __dict__ of the class
"""
