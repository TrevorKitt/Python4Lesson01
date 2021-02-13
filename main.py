class Person:
    def __init__(self, name, age, hair_colour, height, phone_number):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.height = height
        self.phone_number = phone_number

    def get_greeting(self):
        return "Hi, my name is {}".format(self.name)


class Student(Person):
    def __init__(self, name, age, hair_colour, height, phone_number, grade, student_number, parent_name, parent_phone_number, gpa):
        super(Student, self).__init__(name, age, hair_colour, height, phone_number)
        self.grade = grade
        self.student_number = student_number
        self.parent_name = parent_name
        self.parent_phone_number = parent_phone_number
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

class Employee(Person):
    def __init__(self, name, age, hair_colour, height, phone_number, job_title, employee_type):
        super(Employee, self).__init__(name, age, hair_colour, height, phone_number)
        self.job_title = job_title
        self.employee_type = employee_type

person = Person("Sam", 12, "Brown")
print(person.get_greeting())
student = Student("Madeline", 14, "Black", 8, 204534)
print(student.grade)
print(student.get_greeting())


