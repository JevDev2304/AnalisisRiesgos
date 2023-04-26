import tkinter.messagebox
import webbrowser

from UItkinter import UI
from modelo import Program
import tkinter as tk

class Controller:
    def __init__(self,vista:UI,modelo:Program):
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




    def log_in(self):
        try:
            id =self.vista.obtener_info_order()[0]
            password= self.vista.obtener_info_order()[1]
            print(id, password, "ESTO ES LO QUE DA LA VISTA ")
            self.modelo.log_in(id, password)
        except TypeError:
            tk.messagebox.showerror("Llena todos los campos de la encuesta", "Ninguno puede quedar vacio")
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            self.vista.ventana_user_register.destroy()
            self.vista.create_window_log_out(self,id)
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

    def delete_account(self):
        usuario = self.modelo.isLogIn
        nombre = usuario.username
        self.vista.create_window_delete_account(self, nombre)
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
    def open_taxonomy(self):
        webbrowser.open('https://drive.google.com/file/d/1EIllGodINQhz8BxR7LjMzEEdcJP0T8CN/view?usp=sharing')
























