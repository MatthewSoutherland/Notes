"""
@classmethod is a decorator that allows you to define a method that can be called on the class itself rather than on an instance of the class.
cls is the first parameter of a class method. It is a reference to the class itself.    
"""


class People:
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        People.number_of_people += 1

    @classmethod
    def show_number_of_people(cls):
        print(cls.number_of_people)


person1 = People("John", 30)
person2 = People("Alice", 25)
person3 = People("Bob", 40)
People.show_number_of_people()  # Output: 3

"""
This usage does not instantiate the class, so no instance object is created from the Vector_Math class 
when using its static methods in this way. Thus, memory usage is confined to what's necessary for 
the class definitions and the static methods, not instances of the class. Static methods are more like 
functions grouped under the class namespace for organizational and contextual purposes.
This approach minimizes memory usage since no instance objects are created
"""


class Vector_Math:
    @staticmethod
    def add_vectors(vector1, vector2):
        return [vector1[0] + vector2[0], vector1[1] + vector2[1]]

    @staticmethod
    def subtract_vectors(vector1, vector2):
        return [vector1[0] - vector2[0], vector1[1] - vector2[1]]

    @staticmethod
    def dot_product(vector1, vector2):
        return vector1[0] * vector2[0] + vector1[1] * vector2[1]

    @staticmethod
    def cross_product(vector1, vector2):
        return vector1[0] * vector2[1] - vector1[1] * vector2[0]

    @staticmethod
    def scalar_product(vector, scalar):
        return [vector[0] * scalar, vector[1] * scalar]

    @staticmethod
    def magnitude(vector):
        return (vector[0] ** 2 + vector[1] ** 2) ** 0.5

    @staticmethod
    def normalize(vector):
        magnitude = Vector_Math.magnitude(vector)
        return [vector[0] / magnitude, vector[1] / magnitude]


line_one = [1, 2]
line_two = [2, 1]
print(Vector_Math.add_vectors(line_one, line_two))  # Output: [3, 3]
