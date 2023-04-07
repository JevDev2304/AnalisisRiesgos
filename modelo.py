from datetime import *
import re


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
                return print("Error")
        if not self.validar_correo(mail):
            return print("Error")
        birth = self.validar_fecha(birth)
        newUser = User(userName, name, password, birth, mail)
        return newUser

    def log_in(self):
        pass

    def log_out(self):
        pass

    def delete_account(self):
        pass

    def validar_correo(self,correo):
        # Expresión regular para validar el formato del correo electrónico
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        # Verificar si el correo cumple con el patrón de la expresión regular
        if re.match(patron, correo):
            return True
        else:
            return False

    def validar_fecha(self,fecha_string):
        try:
            fecha = datetime.strptime(fecha_string, '%Y-%m-%d %H:%M:%S')
            return fecha
        except ValueError:
            return None

