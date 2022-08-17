"""
    - Topic : Class
    - Source Link : https://www.pythontutorial.net/python-oop/python-class/
"""
#%%
"""
    Class -> Object
    - A container that contains data(state) & functionality(method)
    - Use attributes to model the state(data) of an object
    - Use functions to model thr behaviors
    - The object is created from class, object of a class is also called instance
    - A class is also an object, which is an instance of `type`
"""

#%%


class Person:
    pass


#%%
person = Person()
print(person)  # <__main__.Person object at 0x7fa8775bde50>
print(id(person))  # id() returns the memory address of an object : 140361530868736
print(hex(id(person)))
# turn id to lowercase hexadecimal string prefixed with 0x: 0x7fa8771d6dc0
print(isinstance(person, Person))  # True
print(Person.__name__)  # Person
print(type(Person))  # <class 'type'>
