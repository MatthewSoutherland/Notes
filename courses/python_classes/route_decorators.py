import time

"""
this is a decorator that takes a function as an argument and returns a 
new function that wraps the original function inside it.

"""


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Start time
        result = func(*args, **kwargs)  # Call the function
        end = time.time()  # End time
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


@timer
def example_function(n):
    return sum([i**2 for i in range(n)])


# example_function = timer(example_function)

print(
    example_function(1000000)
)  # Output: example_function took 0.0839998722076416 seconds

"""
the __init__ calls the setter method, which checks if the value is 
negative. the @property decorator is used to define a getter method.
The @radius.setter decorator is used to define a setter method.
Internal Mechanism: In Python, when you call del on an attribute, Python 
internally looks up whether there's a __delete__ method defined for 
that attribute in the descriptor (which @property, @radius.setter, 
and @radius.deleter essentially create). If such a method exists, 
it is called.
    """


class Circle:
    def __init__(self, radius):
        self.radius = radius  # This calls the setter method

    @property
    def radius(self):
        return self._radius  # Return the private attribute

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value  # Store the value in a private attribute

    @radius.deleter
    def radius(self):
        del self._radius


c = Circle(5)
print(c.radius)  # Output: 5
c.radius = 10
print(c.radius)  # Output: 10

# del c.radius

print(dir(Circle))

import inspect

class_methods = inspect.getmembers(Circle, predicate=inspect.isfunction)
print(f"\nclass_methods\n")
print(class_methods)

print(f"\nmethods\n")
methods = [method for method in dir(Circle) if callable(getattr(Circle, method))]
print(methods)
