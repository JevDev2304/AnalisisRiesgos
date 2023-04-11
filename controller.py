import tkinter.messagebox


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
            print(usuario)
            self.modelo.sign_up(usuario[0],usuario[1],usuario[2],usuario[3])
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            tk.messagebox.showinfo("Se ingreso correctamente el usuario","No ocurrio ningún problema")

            self.vista.volver_menu()

    def create_window_order(self):
        self.vista.create_window_order(self)

    def create_window_delete_order(self):
        self.vista.create_window_delete_order(self)




    def log_in(self):
        try:
            id =self.vista.obtener_info_order()[0]
            password= self.vista.obtener_info_order()[1]
            print(id, password, "ESTO ES LO QUE DA LA VISTA ")
            self.modelo.log_in(id, password)
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            tk.messagebox.showinfo("Se Inicio la sesión correctamente","Las credenciales de ingreso son correctas")
            self.vista.ventana_user_register.destroy()
            self.vista.create_window_log_out(self,id)
    def log_out(self):
        try:
            self.modelo.log_out()
        except Exception as error:
            tk.messagebox.showerror(str(error), str(error))
        else:
            self.vista.ventana_log_out.destroy()
            tk.messagebox.showinfo("Se Cerro la sesión correctamente", "No ocurrio ningún problema")
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
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            tk.messagebox.showinfo("Se hizo el cambio de contraseña ","No ocurrio ningún problema")
            self.vista.back_create_window_log_out()
    def getinfodelete_account(self):
        try:
            password=self.vista.obtener_info_delete_account()
            self.modelo.delete_account(self.modelo.isLogIn.username,password)
            self.modelo.log_out()
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            tk.messagebox.showinfo("Se elimino la cuenta","La eliminación se hizo exitosamente")
            self.vista.ventana_delete_account.destroy()
            self.vista.ventana_log_out.destroy()
            self.vista.open_menu()







    def diamante_corte_window(self):
        self.vista.create_window_entry_diamante_corte(self)
    def diamante_bruto_window(self):
        self.vista.create_window_entry_diamante_bruto(self)
    def get_info_diamante_corte(self):
        try:
            diamante_info=self.vista.obtener_info_diamante_corte()
            corte=diamante_info[0]
            tamano=diamante_info[1]
            grabado=diamante_info[2]
            origen=diamante_info[3]

        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:

            self.vista.mostrar_menu_elegir_diamante()

    def get_info_diamante_bruto(self):
        try:
            diamante_info = self.vista.obtener_info_diamante_bruto()
            tamano = diamante_info[0]
            grabado = diamante_info[1]
            origen = diamante_info[2]

        except Exception as error:
            tk.messagebox.showerror(str(error), str(error))
        else:
            self.vista.mostrar_menu_elegir_diamante_bruto()

    def volver_eleccion_diamantes_principal(self):
        self.vista.volver_menu()





















