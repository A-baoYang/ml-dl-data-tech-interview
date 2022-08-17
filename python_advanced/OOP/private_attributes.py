"""
    - Topic : Private attributes
    - Source Link : https://www.pythontutorial.net/python-oop/python-private-attributes/
"""
#%%
"""
    Encapsulation 封裝
    - Hide the internal state of the object from the outside. (information hiding)
    - Control the access of some attributes
"""


class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0


#%%
counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(counter.value())  # 3
# %%
counter.increment()
counter.increment()
counter.current = -999

print(counter.value())  # -999

# %%
"""
    to prevent `current` attribute from modified outside of the Counter class
    => Private attributes
    - can only access from the methods of the class
    - Python actually dont have the concept of private attributes, so we do this by convention and name mangling
    - by convention
        - define by prefixing a single underscore (_attributename)
    - by name mangling
        - prefixing a double underscore (__attribute) and the attribute name in __dict__ will become `_ClassName__attributename`)
"""


class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0


# %%
counter = Counter()

counter._current  # 0

#%%

class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0


# %%
counter = Counter()

counter.__current  # AttributeError

counter._Counter__current  # 0
# %%
