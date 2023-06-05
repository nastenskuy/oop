class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.login_attempts=0
    def describe_user(self):
        print(self.first_name,self.last_name)
    def greeting_user(self):
        print('Привіт',self.first_name,self.last_name,self.age,self.country)
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts=0


user=User('Maria','Kucheruk',19,'Ukraine')
user2=User('Anna','Bak',30,'Germany')
user3=User('Olivia','Parker',23,'UK')
print('№a')
user.describe_user()
user.greeting_user()

user2.describe_user()
user2.greeting_user()

user3.describe_user()
user3.greeting_user()
print('№b')
user.increment_login_attempts()
user.increment_login_attempts()
print('Загалом',user.login_attempts)
user.reset_login_attempts()
print('Скидується',user.login_attempts)