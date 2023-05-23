import tkinter.messagebox
import webbrowser

from UItkinter import UI
from modelo import *
import tkinter as tk

class Controller:
    def __init__(self,vista:UI, modelo : Program):
        self.vista: UI = vista
        self.modelo: Program = modelo
        self.info_temporal =[]
    def start(self):
        self.vista.create_principal_window(self)
    def create_window_user_register(self):
        self.vista.create_window_register(self)
    def getinforegister(self):
        try:
            usuario=self.vista.obtener_info_register()
            self.modelo.sign_up(usuario[0],usuario[1],usuario[2],usuario[3])

        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:

            self.vista.volver_menu()

    def create_window_order(self):
        self.vista.create_window_order(self)
    def create_window_recover_password(self):
        self.vista.create_window_recover_password(self)




    def log_in(self):
        try:
            id =self.vista.obtener_info_order()[0]
            password= self.vista.obtener_info_order()[1]
            self.modelo.log_in(id, password)
        except TypeError:
            tk.messagebox.showerror("Llena todos los campos de la encuesta", "Ninguno puede quedar vacio")
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            self.vista.ventana_user_register.destroy()
            self.vista.create_window_log_out(self,id)
    def recover_password(self):
        try:
            id = self.vista.obtener_info_recover_password()[0]
            mail = self.vista.obtener_info_recover_password()[1]
            self.modelo.recover_password(mail,id)
        except TypeError:
            tk.messagebox.showerror("Llena todos los campos de la encuesta", "Ninguno puede quedar vacio")
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            tk.messagebox.showinfo("Se hizo la validación exitosamente", "Te hemos enviado a tu correo personal la información necesaria para recuperar tu contraseña.")
            self.vista.volver_menu()

    def log_out(self):
        try:
            self.modelo.log_out()
        except Exception as error:
            tk.messagebox.showerror(str(error), str(error))
        else:
            self.vista.ventana_log_out.destroy()
            self.vista.open_menu()
    def change_password(self):
        usuario = self.modelo.isLogIn
        nombre = usuario.username
        self.vista.create_window_change_password(self, nombre)
    def change_username(self):
        usuario = self.modelo.isLogIn
        nombre = usuario.username
        self.vista.create_window_change_username(self, nombre)
    def change_mail(self):
        usuario = self.modelo.isLogIn
        nombre = usuario.username
        self.vista.create_window_change_mail(self, nombre)

    def delete_account(self):
        usuario = self.modelo.isLogIn
        nombre = usuario.username
        self.vista.create_window_delete_account(self, nombre)
    def create_window_log_out_post_change_username(self):
        self.vista.ventana_log_out.destroy()
        self.vista.ventana_change_username.destroy()
        self.vista.create_window_log_out(self,self.modelo.isLogIn.username)
    def create_window_log_out_post_change_mail(self):
        self.vista.ventana_log_out.destroy()
        self.vista.ventana_change_mail.destroy()
        self.vista.create_window_log_out(self,self.modelo.isLogIn.username)

    def getinfochangepassword(self):
        try:
            contrasenias=self.vista.obtener_info_change_password()
            self.modelo.change_password(contrasenias[0],contrasenias[1])
        except TypeError:
            tk.messagebox.showerror("Llena todos los campos de la encuesta", "Ninguno puede quedar vacio")
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            self.vista.back_create_window_log_out()

    def getinfochangeusername(self):
        try:
            info = self.vista.obtener_info_change_username()
            self.modelo.change_username(info[0], info[1])
        except TypeError:
            tk.messagebox.showerror("Llena todos los campos de la encuesta", "Ninguno puede quedar vacio")
        except Exception as error:
            tk.messagebox.showerror(str(error), str(error))
        else:
            self.create_window_log_out_post_change_username()
    def getinfochangemail(self):
        try:
            info = self.vista.obtener_info_change_mail()
            self.modelo.change_mail(info[0], info[1])
        except TypeError:
            tk.messagebox.showerror("Llena todos los campos de la encuesta", "Ninguno puede quedar vacio")
        except Exception as error:
            tk.messagebox.showerror(str(error), str(error))
        else:
            self.create_window_log_out_post_change_mail()
    def getinfodelete_account(self):
        try:
            password=self.vista.obtener_info_delete_account()
            self.modelo.delete_account(self.modelo.isLogIn.username,password)
            self.modelo.log_out()
        except TypeError :
            tk.messagebox.showerror("Llena todos los campos de la encuesta", "Ninguno puede quedar vacio")
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            self.vista.ventana_delete_account.destroy()
            self.vista.ventana_log_out.destroy()
            self.vista.open_menu()
    def my_project(self):
        self.vista.ventana_log_out.withdraw()
        usuario = self.modelo.isLogIn
        nombre = usuario.username
        self.vista.create_window_my_project(self, nombre)

    # RF20 Ver_taxonomia (15)
    def open_taxonomy(self):
        webbrowser.open('https://drive.google.com/file/d/1EIllGodINQhz8BxR7LjMzEEdcJP0T8CN/view?usp=sharing')
    def create_window_delete_risk(self):
        self.vista.create_window_delete_risk(self,self.modelo.isLogIn.username,list(self.modelo.isLogIn.project.myTaxonomy.risks.keys()))
    def create_window_add_risk(self):
        if self.modelo.isLogIn.project.obtenerriesgos_faltantes() != []:
            self.vista.create_window_add_risk(self,self.modelo.isLogIn.username,self.modelo.isLogIn.project.obtenerriesgos_faltantes())
        else:
            self.vista.mostrar_ventana_ya_tienes_todos_los_riesgos()
    def delete_my_risk(self):
        risk = str(self.vista.get_info_delete_risk())
        self.modelo.isLogIn.project.eliminar_riesgo(risk)
        self.vista.volver_my_project()
    def add_my_risk(self):
        risk = str(self.vista.get_info_add_risk())
        self.modelo.isLogIn.project.agregar_riesgo(risk)
        self.vista.volver_my_project_add_risk()

    # RF20 Reiniciar_taxonomia (14)
    def restart_my_tax(self):
        if self.vista.question_restart_taxonomy() == "yes":
            self.modelo.isLogIn.project.myTaxonomy = Taxonomy()
            tk.messagebox.showinfo("No ocurrio ningún problema","Se ha restablecido tu taxonomía satisfactoriamente")



























