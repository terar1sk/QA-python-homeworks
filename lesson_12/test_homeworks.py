import math
import pytest
import allure

from lesson_12.homeworks import(
    sum_csv_numbers,
    Student,
    Diamond,
    Square,
    Rectangle,
    Circle,
)


""" --- HW 11 --- """
@allure.feature("HW11 - CSV Sum")
class TestSumCsvNumbers:

    @allure.title("Sum of positive numbers")
    def test_sum_ok(self):
        with allure.step("Call sum_csv_numbers with '1,2,3,4'"):
            result = sum_csv_numbers("1,2,3,4")
        with allure.step("Check result equals 10"):
            assert result == 10

    @allure.title("Sum with negative numbers")
    def test_sum_negative(self):
        with allure.step("Call sum_csv_numbers with '-1,2,-3'"):
            result = sum_csv_numbers("-1,2,-3")
        with allure.step("Check result equals -2"):
            assert result == -2

    @allure.title("Invalid input raises ValueError")
    def test_sum_error(self):
        with allure.step("Call sum_csv_numbers with invalid string 'qwerty1,2,3'"):
            with pytest.raises(ValueError):
                sum_csv_numbers("qwerty1,2,3")


""" --- HW 10 --- """
@allure.feature("HW10 - Figures")
class TestFigures:

    @allure.title("Square area calculation")
    def test_square(self):
        with allure.step("Create Square with side=5"):
            s = Square(5)
        with allure.step("Check area equals 25"):
            assert s.area() == 25

    @allure.title("Rectangle perimeter calculation")
    def test_rectangle(self):
        with allure.step("Create Rectangle with w=3, h=7"):
            r = Rectangle(3, 7)
        with allure.step("Check perimeter equals 20"):
            assert r.perimeter() == 20

    @allure.title("Circle area calculation")
    def test_circle(self):
        with allure.step("Create Circle with radius=2.5"):
            c = Circle(2.5)
        with allure.step("Check area equals π * 6.25"):
            assert math.isclose(c.area(), math.pi * 6.25)


""" --- HW 9 --- """
@allure.feature("HW9 - Diamond")
class TestDiamond:

    @allure.title("Diamond beta angle is calculated correctly")
    def test_diamond_valid(self):
        with allure.step("Create Diamond with side=10, alpha=60"):
            d = Diamond(10, 60)
        with allure.step("Check beta equals 120"):
            assert d.beta == 120

    @allure.title("Two equal diamonds are equal")
    def test_diamond_eq(self):
        with allure.step("Create two identical Diamonds"):
            d1 = Diamond(10, 60)
            d2 = Diamond(10, 60)
        with allure.step("Check they are equal"):
            assert d1 == d2

    @allure.title("Diamond multiplication scales side")
    def test_diamond_mul(self):
        with allure.step("Create Diamond with side=5, alpha=60"):
            d = Diamond(5, 60)
        with allure.step("Multiply diamond by 2"):
            d2 = d * 2
        with allure.step("Check new side equals 10"):
            assert d2.side == 10

    @allure.title("Negative side raises ValueError")
    def test_diamond_error(self):
        with allure.step("Try to create Diamond with negative side"):
            with pytest.raises(ValueError):
                Diamond(-1, 60)


""" --- HW 8 --- """
@allure.feature("HW8 - Student")
class TestStudent:

    @allure.title("Change student average grade")
    def test_student_change_grade(self):
        with allure.step("Create Student with grade=80"):
            s = Student("A", "B", 20, 80)
        with allure.step("Change grade to 90"):
            s.change_average_grade(90)
        with allure.step("Check grade equals 90"):
            assert s.average_grade == 90

    @allure.title("Student info contains full name")
    def test_student_info(self):
        with allure.step("Create Student with name 'A B'"):
            s = Student("A", "B", 20, 80)
        with allure.step("Check info contains 'A B'"):
            assert "A B" in s.info()