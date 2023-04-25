class version1:

    def button(self):
        print("colour yellow")

class version2(version1):

    def button(self):
        print("colour red")

a=version2()

a.button()