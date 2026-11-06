class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  

    def check_password(self, password):
        return self.__password == password


u = User("alex", "qwerty123")
print(u.check_password("qwerty123")) 
print(u.check_password("wrong"))      