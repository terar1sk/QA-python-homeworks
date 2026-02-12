from abc import ABC, abstractmethod
import math


""" ---- HW 10.1 ---- """
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(
        self,
        name: str,
        salary: float,
        department: str,
        programming_language: str,
        team_size: int,
    ):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

""" ---- HW 10.1 Tests ---- """
def test_teamlead():
    tl = TeamLead("Dmytro", 5000, "QA", "Python", 13)

    assert hasattr(tl, "name")
    assert hasattr(tl, "salary")
    assert hasattr(tl, "department")
    assert hasattr(tl, "programming_language")
    assert hasattr(tl, "team_size")
    print("Test TeamLead passed")


""" ---- HW 10.2 ---- """
class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Square(Figure):
    def __init__(self, side: float):
        self.__side = side

    def area(self) -> float:
        return self.__side ** 2

    def perimeter(self) -> float:
        return 4 * self.__side


class Rectangle(Figure):
    def __init__(self, w: float, h: float):
        self.__w = w
        self.__h = h

    def area(self) -> float:
        return self.__w * self.__h

    def perimeter(self) -> float:
        return 2 * (self.__w + self.__h)


class Circle(Figure):
    def __init__(self, r: float):
        self.__r = r

    def area(self) -> float:
        return math.pi * self.__r ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.__r


def demo_figures():
    shapes = [
        Square(5),
        Rectangle(3, 7),
        Circle(2.5),
    ]

    print("\nФигура:")
    for s in shapes:
        print(
            f"{s.__class__.__name__}: "
            f" S = {s.area():.2f}, "
            f" P = {s.perimeter():.2f}"
        )



#main
if __name__ == "__main__":
    test_teamlead()
    demo_figures()