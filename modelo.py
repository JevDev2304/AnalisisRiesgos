from validacionesFront import *


class User:
    def __init__(self, username: str, name: str, password: str, birth: datetime, mail: str):
        self.username = username
        self.name = name
        self.password = password
        self.birth = birth
        self.datetime = datetime
        self.mail = mail


class Administrator(User):
    def __init__(self, username: str, name: str, password: str, birth: datetime, mail: str):
        User.__init__(username, name, password, birth, mail)


class Program:

    def __init__(self):
        self.user_list = []

    # REQUISITOS
    def sign_up(self, userName, name, password, birth, mail):
        for user in self.user_list:
            if user.username == userName:
                raise ElUsuarioYaExiste()
            else:
                newUser = User(userName, name, password, birth, mail)
                self.user_list.append(newUser)
                return None
    def log_in(self,username,pasword):
        for user in self.user_list:
            if user.username is username and user.password is pasword:
                return True
            else:
                raise CredencialesNoValidas()



    def log_out(self):
        pass

    def delete_account(self):
        pass







