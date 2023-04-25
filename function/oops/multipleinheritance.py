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

class studentfaculty(student,faculty):
    pass
sf1=studentfaculty()
sf1.login()
sf1.greet_student()        