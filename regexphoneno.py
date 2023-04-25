import re
phn=(input("enter the number:"))
r=re.fullmatch("[0-9]",phn)
if (r==None):
    print("enter valid number")
else:
    print("verified")
        
