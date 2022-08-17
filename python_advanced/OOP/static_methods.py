"""
    - Topic : Static methods
    - Source Link : https://www.pythontutorial.net/python-oop/python-static-methods/
"""

#%%
"""
    Class methods
    - static methods are bound to an object
    - class methods can access & modify the object state 
    - Python implicity pass `cls` argument to class methods
    - use @classmethod decorators to define

    Static methods
    - Use for defining utility methods or group of functions that have logical relationships in a class
    - static methods not bound to an object
    - static methods cannot access & modify the object state 
    - Python doesn't implicity pass `cls` argument to static methods
    - use @staticmethod decorators to define
"""


class TemperatureConverter:
    KEVIN = ("K",)
    FAHRENHEIT = "F"
    CELSIUS = "C"

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5 * (f + 459.67) / 9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9 * k / 5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ""
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = "°F"
        elif unit == TemperatureConverter.CELSIUS:
            symbol = "°C"
        elif unit == TemperatureConverter.KEVIN:
            symbol = "°K"

        return f"{value}{symbol}"


# %%
f = TemperatureConverter.celsius_to_fahrenheit(35)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))

# %%
