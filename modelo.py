import datetime
import json

import send_email
from send_email import *
class User:
    project = None
    mail = None
    password = None
    name = None
    username = None
    def __init__(self, username: str, name: str, password: str, mail: str ):

        self.username = username
        self.name = name
        self.password = password
        self.datetime = datetime
        self.mail = mail
        self.project = Project()


class Project:

    def  __init__(self):
        self.myTaxonomy: Taxonomy = Taxonomy()

    # RF09 Eliminar riesgos
    # RF07 Mostrar_taxonomia
    def eliminar_riesgo(self,nombreRiesgo  :  str):
        self.myTaxonomy.risks.pop(nombreRiesgo)

    # RF04 agregar_riesgo
    def agregar_riesgo(self,nombreRiesgo : str):
        for riesgo in list(self.myTaxonomy.risks.keys()):
            if riesgo == nombreRiesgo:
                raise Exception("El riesgo ya esta agregado en la taxonomia")
        else:
            self.myTaxonomy.risks[nombreRiesgo] = Taxonomy().risks[nombreRiesgo]
    def obtenerriesgos_faltantes(self):
        listaDeMisRiesgos = list(self.myTaxonomy.risks.keys())
        listaTodosLosRiesgos = list(Taxonomy().risks.keys())
        listaRiesgosFaltantes = []
        if len(listaDeMisRiesgos) == len(listaTodosLosRiesgos):
            return []
        for riesgo in listaTodosLosRiesgos:
            if riesgo not in listaDeMisRiesgos:
                listaRiesgosFaltantes.append(riesgo)
        return listaRiesgosFaltantes





class Taxonomy:
    def __init__(self):
        self.risks = {"Requerimientos":"Tiene requerimientos bien definidos.",
                "Design": "La traducción de los requerimientos al diseño del software es sencilla.",
                "Pruebas unitarias": "El software cuenta con pruebas unitarias.",
                "Especialidades ingenieria": "El software es seguro, fiable y se encuentra protegido.",
                "Recursos": "Las condiciones de tiempos, personal y fechas  han sido cumplidas",
                "Contrato": "Se estan cumpliendo los terminos y condiciones firmados en el contrato",
                "Intermediarios": "No hay ningún tipo de problema con los intermediarios del proyecto",
                "Proceso":"El proceso de desarrollo,desde la planeación hasta la documentación esta siendo bien implementado",
                "Sistema": "Tienen todas las herramientas necesarias para desarrollar el proyecto",
                "Presupuesto": "Poseen de el presupuesto necesario para el proyecto",
                "Tiempos": "Hay cumplimiento de avance en las fechas estipuladas por el equipo de desarrollo",
                "Cooperacion": "Hay cooperación y buena actitud en el equipo de trabajo",
                }
    def clean_tax(self):
        self.risks = {}




class Program:

    def __init__(self):
        self.user_list = []
        self.isLogIn = None

    # RF16 Guardar_información (12)
    def read_json(self):
        json_document = open("database.json",mode="r")
        json_str = json_document.read()
        dictionary = dict(json.loads(json_str))
        return dictionary
    def load_json(self,dictionary_json):
        listaUsuarios = dictionary_json["Usuarios"]
        for usuario in listaUsuarios:
            self.sign_up(usuario["name"], usuario["username"], usuario["mail"], usuario["password"])
            lista_riesgos = usuario["taxonomia"]
            self.user_list[-1].project.myTaxonomy.clean_tax()
            for riesgo in lista_riesgos:
                self.user_list[-1].project.agregar_riesgo(riesgo)
    def save_json(self):
        dict_python_to_json = {"Usuarios": []}
        for user in self.user_list:
            dict_python_user = {"username": user.username, "name": user.name, "password": user.password, "mail": user.mail, "taxonomia": list(user.project.myTaxonomy.risks.keys())}
            dict_python_to_json["Usuarios"].append(dict_python_user)
        with open("database.json","w") as outfile:
            json.dump(dict_python_to_json,outfile,indent=4)







    #RF01 Registrar_Usuario
    def sign_up(self, name, username, mail, password):
        for user in self.user_list:
            if user.username == username:
                raise Exception("ya existe un usuario con el nombre de usuario ingresado, cambia tu nombre de usuario para poder registrarte")
        else:
         newUser = User(username, name, password, mail)
         self.user_list.append(newUser)

    # RF02 Iniciar_sesión
    def log_in(self,username,password):
        for user in self.user_list:
            if (user.username == username) and (user.password == password):
                self.isLogIn = user
        if self.isLogIn == None:
            raise Exception("Credenciales no validas")

    # RF03 Cerrar_sesion
    def log_out(self):
        if self.isLogIn != None:
            self.isLogIn = None
        elif self.isLogIn == None:
            raise Exception("No hay una sesion abierta")

    # RF13 Cambiar_contraseña (11)
    def change_password(self,old_password,new_password):
        if old_password == new_password:
            raise Exception("La nueva contraseña es igual a la antigua, si deseas cambiarla tiene que ser una nueva")
        user = self.isLogIn
        if user.password != old_password:
            raise Exception("La contraseña antigua no esta bien ingresada,no se puede cambiar la contraseña sin haber hecho la validación.")
        else:
            user.password = new_password

    # RF08 Cambiar_nombre_usuario
    def change_username(self,username,password):
        if username == self.isLogIn.username:
            raise Exception("El usuario es igual al anterior, intentalo nuevamente")
        if password != self.isLogIn.password:
            raise Exception("La contraseña antigua no esta bien ingresada,no se puede cambiar el correo sin haber hecho la validación.")
        username_is_repeat = False
        for user in self.user_list:
            if user.username == username:
                raise Exception("El usuario ya existe, intenta uno nuevo")
        if username_is_repeat is False:
            self.isLogIn.username = username

    # RF10 Cambiar_correo_electronico
    def change_mail(self,mail,password):
        if mail == self.isLogIn.mail:
            raise Exception("El correo es igual al anterior, intentalo nuevamente")
        if password != self.isLogIn.password:
            raise Exception("La contraseña antigua no esta bien ingresada,no se puede cambiar el correo sin haber hecho la validación.")
        mail_is_repeat = False
        for user in self.user_list:
            if user.mail == mail:
                raise Exception("Este correo ya se encuentra registrado en otra cuenta, intenta  con uno nuevo")
        if mail_is_repeat is False:
            self.isLogIn.mail = mail

    # RF05 Recuperar_contraseña
    def recover_password(self,mail, username):
        asunto = f"Recuperación contraseña:"
        lista_correos = []
        lista_usernames =[]
        password = ""
        for usuario in self.user_list:
            if (usuario.mail == mail) and (usuario.username == username):
                password = usuario.password
            lista_correos.append(usuario.mail)
            lista_usernames.append(usuario.username)
        if mail not in lista_correos:
            raise Exception("Correo no existe")
        if username not in lista_usernames:
            raise Exception ("Usuario no existe")
        message = f"Este es un correo automático para recuperar su usuario o contraseña.\nCorreo : {mail}\nNombre de usuario : {username}\n Contraseña:  {password} \n Si no pediste recuperación de contraseña no compartas esta información."
        enviar_correo(mail,asunto,message)

    # RF19 Guardar_información (13)
    def delete_account(self,username,password):
        usuarioExiste = 0
        for user in self.user_list:
            if (user.username == username) and (user.password == password):
                self.user_list.remove(user)
                usuarioExiste = 1
        if usuarioExiste == 0:
            raise Exception("Ingresaste mal la contraseña", "Intenta de nuevo")































