"""
    - Topic : Object-oriented programming
    - Source link : https://www.pythontutorial.net/python-oop/python-object-oriented-programming/
"""

#%%
"""
    Define class, instance attributes, instance methods, class attributes, class methods
"""


class Person:
    # class attribute : shared by all instances of the class
    counter = 0

    def __init__(self, name, age):
        """define instance attributes"""
        self.name = name
        self.age = age
        # cumulate add the number to the class attributes: counter
        Person.counter += 1

    def greet(self):
        """define instance methods"""
        return f"Hi, it's {self.name}."

    # class method : shared by all instances of the class
    @classmethod
    def create_anonymous(cls):
        """
        Use for high frequency function
        - cls: the class itself
        """
        return Person("Anonymous", 22)


#%%
p1 = Person("John", 25)
p2 = Person("Jerry", 26)
print(Person.counter)  # 2
anonymous = Person.create_anonymous()
print(anonymous.name)  # Anonymous
print(Person.counter)  # 3

#%%
"""
    Define static method
"""


class TemperatureConverter:
    # static method : not bound to any instances
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9


#%%
f_temp = TemperatureConverter.celsius_to_fahrenheit(30)
print(f_temp)  # 86.0

# %%
"""
    Single inheritance
    - child class can access parent class attributes
    - child class can extend parent class by adding new attributes
    - child class can override parent class instance methods
"""


class Employee(Person):
    """inheriting from class: `Person`"""

    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f" I'm a {self.job_title}."


#%%
employee = Employee("John", 25, "Python Engineer")
print(employee.greet())
# %%
