import math
import pytest

from lesson_12.homeworks import(
    sum_csv_numbers,
    Student,
    Diamond,
    Square,
    Rectangle,
    Circle,
)


""" --- HW 11 --- """
def test_sum_ok():
    assert sum_csv_numbers("1,2,3,4") == 10

def test_sum_negative():
    assert sum_csv_numbers("-1,2,-3") == -2

def test_sum_error():
    with pytest.raises(ValueError):
        sum_csv_numbers("qwerty1,2,3")


""" --- HW 10 --- """
def test_square():
    s = Square(5)
    assert s.area() == 25

def test_rectangle():
    r = Rectangle(3, 7)
    assert r.perimeter() == 20

def test_circle():
    c = Circle(2.5)
    assert math.isclose(c.area(), math.pi * 6.25)


""" --- HW 9 --- """
def test_diamond_valid():
    d = Diamond(10, 60)
    assert d.beta == 120

def test_diamond_eq():
    assert Diamond(10, 60) == Diamond(10, 60)

def test_diamond_mul():
    d = Diamond(5, 60)
    d2 = d * 2
    assert d2.side == 10

def test_diamond_error():
    with pytest.raises(ValueError):
        Diamond(-1, 60)


""" --- HW 8 --- """
def test_student_change_grade():
    s = Student("A", "B", 20, 80)
    s.change_average_grade(90)
    assert s.average_grade == 90

def test_student_info():
    s = Student("A", "B", 20, 80)
    assert "A B" in s.info()