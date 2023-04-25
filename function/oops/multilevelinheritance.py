#parent class named (user)
class user:
    def register(self):
        print("registering")

    def login(self):
        print("logging in")
# child class named (student)
class student(user):
    def greet_student(self):
        print("hi student")
#child class named(faculty)
class faculty(user):
    def greet_faculty(self):
        print("hello teacher")
#grand child class named(tempofaculty)
class tempofaculty(faculty):
    def greet_faculty(self):
        print("hello .. nice to meet you")        

#creating a object named(stud1)
stud1=student()
#funcction calling
stud1.greet_student()
#child class calling
fac1=faculty()
fac1.greet_faculty()

stud1.login()

tempofaculty1=tempofaculty()
tempofaculty1.greet_faculty()

tempofaculty1.login()