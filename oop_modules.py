# ==========================================
# Topic 5: Object-Oriented Programming (OOP)
# ==========================================

# Base Class (Encapsulation)
class Person:
    def __init__(self, name: str, age: int):
        self.name = name          # Public attribute
        self.__age = age          # Private attribute

    def get_age(self):
        return self.__age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.__age}"

# Derived Class (Inheritance & Polymorphism)
class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    # Overriding method (Polymorphism)
    def display_info(self):
        return f"Student: {self.name} | ID: {self.student_id} | Age: {self.get_age()}"


if __name__ == "__main__":
    student = Student("SSALI Ronnie", 22, "VU-BAD-2607-4467-DAY")
    print(student.display_info())