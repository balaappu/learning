

class user:
    def __init__(self,user_name,pwd):
        self.user_name=user_name
        self.pwd=pwd

    def register(self):
        print("registering"+ self.user_name)

    def login(self):
        print("logging in"+" " +self.user_name)


user1=user("ravi",7578)
user2=user("ram",3039)
user3=user("renu",9909)


user3.register()
user2.login()