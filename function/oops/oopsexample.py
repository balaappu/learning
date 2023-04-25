class user:
    def __init__(self,user_name,pwd):
        self.user_name=user_name
        self.pwd=pwd

    def register(self):
        print("registering..")

    def login(self):
        print("logging in...")

user1 =user("ravi",7578)
user2=user("ram",8900)
user3=user("muthu",5678)

user1.register()
user3.login()

print(user1.user_name)
print(user3.pwd)
