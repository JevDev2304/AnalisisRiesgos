import datetime
class User:
    def __init__(self, username: str, name: str, password: str, mail: str):
        self.username = username
        self.name = name
        self.password = password
        self.datetime = datetime
        self.mail = mail






class Program:

    def __init__(self):
        self.user_list = [User("prueba","prueba","prueba","prueba")]
        self.isLogIn = None

    # REQUISITOS
    def sign_up(self, name, username, mail, password):
        for user in self.user_list:
            if user.username == username:
                raise Exception("ya existe un usuario con el nombre de usuario ingresado, cambia tu nombre de usuario para poder registrarte")
        else:
         newUser = User(username, name, password, mail)
         print(newUser.username + " " + password)
         self.user_list.append(newUser)

    def log_in(self,username,password):
        for user in self.user_list:
            if (user.username == username) and (user.password == password):
                self.isLogIn = user
        if self.isLogIn == None:
            raise Exception("Credenciales no validas")

    def log_out(self):
        if self.isLogIn != None:
            self.isLogIn = None
        elif self.isLogIn == None:
            raise Exception("No hay una sesion abierta")
    def change_password(self,old_password,new_password):
        if old_password == new_password:
            raise Exception("La nueva contraseña es igual a la antigua, si deseas cambiarla tiene que ser una nueva")
        user = self.isLogIn
        if user.password != old_password:
            raise Exception("La contraseña antigua no esta bien ingresada,no se puede cambiar la contraseña sin haber hecho la validación.")
        else:
            user.password = new_password

    def delete_account(self,username,password):
        usuarioExiste = 0
        for user in self.user_list:
            if (user.username == username) and (user.password == password):
                self.user_list.remove(user)
                usuarioExiste = 1
        if usuarioExiste == 0:
            raise Exception("Ingresaste mal la contraseña", "Intenta de nuevo")





























