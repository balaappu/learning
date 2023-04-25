class user:
    def register(self):
        print("registering")

    def login(self):
        print("logging in")
        
    def greet(self):
        print("hello user")    
# child class named (student)
class student(user):
    def greet(self):
        print("hi student")
#child class named(faculty)
class faculty(user):
    def greet(self):
        print("hello teacher")
#grand child class named(tempofaculty)
class tempofaculty(faculty):
    def greet(self):
        print("hello .. nice to meet you")        


stud1=student()
stud1.greet()
        
fac1=faculty()
fac1.greet()

tempfact1=tempofaculty()
tempfact1.greet()
