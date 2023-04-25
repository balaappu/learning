def add():
    a=int(input("enter the value of A:"))
    b=int(input("enter the value of B:"))
    c=a+b
    return c
def multi():
    a=int(input("enter the value of A:"))
    b=int(input("enter the value of B:"))
    c=a*b
    return c
def div():
    a=int(input("enter the value of A:"))
    b=int(input("enter the value of B:"))

    c=a/b
    return c
def sub():
    a=int(input("enter the value of A:"))
    b=int(input("enter the value of B:"))
    c=a-b
    return c
def calc():
  print("addition:1","subraction:2","division:3","multiplication:4","Exit:0")
  print("enter your choice")
  choice=int(input("enter your choice:"))

  if choice == 1:
    c=add()
    print("Result: ",c)
    calc()
  elif choice == 2:
    c=sub()
    print("Result: ",c)
    calc()
  elif choice == 3:
    c=div()
    print("Result: ",c)
    calc()
  elif choice == 4:
    c=multi()
    print("Result: ",c)
    calc()
  elif choice == 0:
    print("Thank you")
  else:
    print("exit")

calc()




print("A")