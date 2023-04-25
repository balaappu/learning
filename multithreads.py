import threading
import time
#defining a function
def updated_db():
    print("data updating...")
#using time.sleep method making delay time of first function output to nested function("data updated") delay time 5 sec    
    time.sleep(5)
    print("data updated...")

def display_nums(num):
    for i in range(1,num+1):
        print(i)
#calling the function
display_nums(5)
updated_db()
#the output clearly show in multithreading concept using time function...            