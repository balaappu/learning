#importing thread
from threading import*
#defining a class named "A",
class A(Thread):
# defining a function    
    def run(self):
        for i in range(5):
         print("one")
#defining a class named "B"
class B(Thread):
# defining a function    
    def run(self):
        for i in range(5):
            print("B")
#Object created for class, object name:a
a=A()
b=B()
#calling the class function
a.start()
b.start()