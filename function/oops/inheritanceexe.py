class user:
    def register(self):
        print("registering")

    def login(self):
        print("logging in")


class student(user):
    def greet_student(self):
        print("hi student")

class faculty(user):
    def greet_faculty(self):
        print("hello teacher")                    

stud1=student()
stud1.greet_student()  

fac1=faculty()
fac1.greet_faculty()

stud1.login()