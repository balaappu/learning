import re
email=str(input("enter your email id:"))
r=re.fullmatch(r" \b[A-Z a-z 0-9 ._%+-]+ @\[A-Z a-z 0-9.-]+\.[A-Z a-z]\b",email)
if (r==None):
    print("please, enter the correct e-mail")
else:
    print("verified")

    