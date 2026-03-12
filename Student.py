# Base class
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Derived class
class Student(Person):
    def __init__(self, id, name, semester, marks1, marks2):
        # Call the constructor of Person
        super().__init__(id, name)
        self.semester = semester
        self.marks1 = marks1
        self.marks2 = marks2

    # Method to calculate average marks
    def calculate_average(self):
        avg = (self.marks1 + self.marks2) / 2
        return avg


# Example usage
s1 = Student(101, "Rahul", 2, 85, 90)

print("ID:", s1.id)
print("Name:", s1.name)
print("Semester:", s1.semester)
print("Average Marks:", s1.calculate_average())