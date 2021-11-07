class Student():
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def __repr__(self):
        return f"Student name: {self.name}, student age: {self.age}, student class: {self.class_}"

    def greet(self):
        return f"Hello {self.name}"



stud1 = Student("John", 24, "geography")
stud2 = Student("Dave", 24, "geography")
stud3 = Student("Sam", 24, "geography")
stud4 = Student("Joe", 24, "geography")
stud5 = Student("Denise", 24, "geography")

print(stud1)
print(stud2)
print(stud3)
print(stud4)
print(stud5)

