"""
    - Topic : Class attributes
    - Source Link : https://www.pythontutorial.net/python-oop/python-class-attributes/
"""

#%%
"""
    When to use Python class attributes
    1. Storing class constants
       - constant which shouldn't change in each instance
    2. Tracking data across all instances
       - collect or accumulate everytime creating a new instance from class
    3. Defining default values
       - same default value for all instance methods of a class
"""


class Circle:
    circle_list = []
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        # add the instance to the circle list
        self.circle_list.append(self)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(10)
c2 = Circle(20)

print(len(Circle.circle_list))  # 2

#%%
class Product:
    default_discount = 0

    def __init__(self, price):
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self, discount):
        self.discount = discount

    def net_price(self):
        return self.price * (1 - self.discount)


p1 = Product(100)
print(p1.net_price())  # 100

p2 = Product(200)
p2.set_discount(0.05)
print(p2.net_price())  # 190
# %%
