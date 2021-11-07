from testing import Student

def test_Students():
    stud1 = Student("John", 24, "geography")
    assert stud1.greet() == "Hello John"
    

def test_Students2():
    stud1 = Student("John", 24, "geography")
    assert stud1.age == 40