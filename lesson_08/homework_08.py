class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

    def info(self):
        print(f"Студент: {self.first_name} {self.last_name}")
        print(f"Возраст: {self.age}")
        print(f"Средний балл: {self.average_grade}")

student1 = Student("Dmytro", "Isai", 20, 89)
student1.info()

student1.change_average_grade(95)
print("\nПосле изменения среднего балла:")
student1.info()