from abc import ABC, abstractmethod
import math


""" --- HW 11 --- """
def sum_csv_numbers(s: str) -> int:
    parts = s.split(",")
    total = 0
    for p in parts:
        total += int(p)
    return total


""" --- HW 10 --- """
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side


class Rectangle(Figure):
    def __init__(self, w, h):
        self.__w = w
        self.__h = h

    def area(self):
        return self.__w * self.__h

    def perimeter(self):
        return 2 * (self.__w + self.__h)


class Circle(Figure):
    def __init__(self, r):
        self.__r = r

    def area(self):
        return math.pi * self.__r ** 2

    def perimeter(self):
        return 2 * math.pi * self.__r


""" --- HW 9 --- """
class Diamond:
    def __setattr__(self, name, value):
        if name == "side":
            if not isinstance(value, (int, float)):
                raise TypeError
            if value <= 0:
                raise ValueError
            object.__setattr__(self, name, value)

        elif name == "alpha":
            if not isinstance(value, (int, float)):
                raise TypeError
            if not (0 < value < 180):
                raise ValueError
            object.__setattr__(self, "beta", 180 - value)
            object.__setattr__(self, name, value)

        elif name == "beta":
            raise AttributeError

        else:
            object.__setattr__(self, name, value)

    def __init__(self, side, alpha):
        self.side = side
        self.alpha = alpha

    def __eq__(self, other):
        return isinstance(other, Diamond) and self.side == other.side and self.alpha == other.alpha

    def __len__(self):
        return int(self.side)

    def __mul__(self, scale):
        if scale <= 0:
            raise ValueError
        return Diamond(self.side * scale, self.alpha)

    __rmul__ = __mul__


""" --- HW 8 --- """
class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

    def info(self):
        return f"{self.first_name} {self.last_name}, age={self.age}, grade={self.average_grade}"
