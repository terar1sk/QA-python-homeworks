from __future__ import annotations
import random
from typing import List
from sqlalchemy import(
    create_engine,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    select,
)
from sqlalchemy.orm import DeclarativeBase, relationship, Session

DB_URL = "sqlite:///students.db"


# ========================= base =========================
class Base(DeclarativeBase):
    pass


# ========================= таблица связи =========================
enrollments = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", ForeignKey("students.id", ondelete="CASCADE"), primary_key=True),
    Column("course_id", ForeignKey("courses.id", ondelete="CASCADE"), primary_key=True),
)


# ========================= таблицы =========================
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    courses = relationship("Course", secondary=enrollments, back_populates="students")
    def __repr__(self) -> str:
        return f"Student(id={self.id}, name={self.name!r})"


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False, unique=True)
    students = relationship("Student", secondary=enrollments, back_populates="courses")
    def __repr__(self) -> str:
        return f"Course(id={self.id}, title={self.title!r})"


# ========================= функционал =========================
def seed_data(session: Session) -> None:
    course_titles = ["QA Basics", "Python", "Databases", "Web Testing", "Automation"]
    courses = [Course(title=t) for t in course_titles]
    session.add_all(courses)
    session.flush()
    first_names = ["Dmytro", "Anna", "Oleh", "Iryna", "Max", "Sofia", "Ivan", "Olena", "Taras", "Maria"]
    last_names = ["Shevchenko", "Koval", "Bondarenko", "Melnyk", "Kravets", "Isai", "Tkachenko"]
    students: List[Student] = []
    for _ in range(20):
        s = Student(name=f"{random.choice(first_names)} {random.choice(last_names)}")
        s.courses = random.sample(courses, k=random.randint(1, 3))
        students.append(s)
    session.add_all(students)
    session.commit()


def add_student_to_course(session: Session, student_name: str, course_title: str) -> None:
    course = session.scalar(select(Course).where(Course.title == course_title))
    if not course:
        raise ValueError(f"Course not found: {course_title}")
    student = Student(name=student_name)
    student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"Added {student} to {course}")


def students_by_course(session: Session, course_title: str) -> None:
    course = session.scalar(select(Course).where(Course.title == course_title))
    if not course:
        print("Course not found")
        return
    print(f"\nStudents on course '{course.title}':")
    for s in course.students:
        print(" -", s.name)


def courses_by_student(session: Session, student_name: str) -> None:
    student = session.scalar(select(Student).where(Student.name == student_name))
    if not student:
        print("Student not found")
        return
    print(f"\nCourses for student '{student.name}':")
    for c in student.courses:
        print(" -", c.title)


def update_student_name(session: Session, old_name: str, new_name: str) -> None:
    student = session.scalar(select(Student).where(Student.name == old_name))
    if not student:
        print("Student not found for update")
        return
    student.name = new_name
    session.commit()
    print(f"Updated student name: {old_name!r} -> {new_name!r}")


def delete_student(session: Session, student_name: str) -> None:
    student = session.scalar(select(Student).where(Student.name == student_name))
    if not student:
        print("Student not found for delete")
        return
    session.delete(student)
    session.commit()
    print(f"Deleted student: {student_name!r}")


# ========================= main =========================
def main() -> None:
    engine = create_engine(DB_URL, echo=False)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        seed_data(session)
        add_student_to_course(session, "New Student", "Python")
        students_by_course(session, "Python")
        courses_by_student(session, "New Student")

        update_student_name(session, "New Student", "New Student Updated")
        courses_by_student(session, "New Student Updated")

        delete_student(session, "New Student Updated")
        courses_by_student(session, "New Student Updated")

if __name__ == "__main__":
    main()