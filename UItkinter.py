import tkinter as tk
import tkinter.messagebox

class PrincipalWindow:
    def __init__(self):
        self.ventana = tk.Tk()



class UI:
    def __init__(self):
        self.principal_window = None
        self.logo = None

    def load_images(self):
        self.logo = tk.PhotoImage(file="imagenes/Analisis De Riesgos.png")
        self.logo = self.logo.subsample(2)
        self.logo_pequeno = self.logo.subsample(2)
        self.user_register = tk.PhotoImage(file="imagenes/Registrar Usuario (300 × 150 px).png")
        self.sesion_start = tk.PhotoImage(file="imagenes/IniciarSesion.png")

        self.register_name = tk.PhotoImage(file="imagenes/NombreCompletoAnalisis.png")
        self.register_username = tk.PhotoImage(file="imagenes/NombreUsuarioAnalisis.png")
        self.register_mail = tk.PhotoImage(file="imagenes/correoRegistroAnalisRiesgo.png")
        self.register_password = tk.PhotoImage(file="imagenes/ContraseñaRegistroAnalisisRiesgo.png")
        self.small_register_password= tk.PhotoImage(file="imagenes/ContraseniaPequena.png")
        self.log_out = tk.PhotoImage(file="imagenes/CerrarSesion.png")
        self.change_password = tk.PhotoImage(file="imagenes/CambiarContraseñaSesion.png")
        self.actual_password = tk.PhotoImage(file="imagenes/ContraseñaActual.png")
        self.new_password = tk.PhotoImage(file="imagenes/NuevaContraseña.png")
        self.delete_account = tk.PhotoImage(file="imagenes/EliminarCuenta.png")
        self.verify_password = tk.PhotoImage(file="imagenes/VerificarContraseña.png")
        self.my_project = tk.PhotoImage(file = "imagenes/miProyecto.png")
        self.see_taxonomy = tk.PhotoImage(file="imagenes/verTaxonomia.png")
        self.delete_risk = tk.PhotoImage(file = "imagenes/EliminarRiesgo.png")
        self.restart_taxonomy = tk.PhotoImage(file = "imagenes/RestablecerTaxonomia.png")

        self.register_name_small = self.register_name.subsample(2)
        self.register_username_small = self.register_username.subsample(2)
        self.register_mail_small = self.register_mail.subsample(2)
        self.register_password_small = self.register_password.subsample(2)

        self.menu = tk.PhotoImage(file="imagenes/DevolverseMenuPrincipal.png")




    def volver_menu(self):
        self.ventana_user_register.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")

    def open_menu(self):
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")
    def volver_menu_inicio_sesion(self, username):
        self.ventana_user_register.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")
        self.principal_window.ventana.title("Usuario: " + username)

    def back_create_window_log_out(self):
        self.ventana_change_password.destroy()
        self.ventana_log_out.iconify()
        self.ventana_log_out.state("zoomed")

    def back_create_window_log_out_delete_account(self):
        self.ventana_delete_account.destroy()
        self.ventana_log_out.iconify()
        self.ventana_log_out.state("zoomed")
    def back_my_proyect_window_log_out(self):
        self.ventana_my_project.destroy()
        self.ventana_log_out.iconify()
        self.ventana_log_out.state("zoomed")

    def obtener_info_order(self):
            id = self.entry_id.get()
            password = self.entry_password.get()
            if " " in id:
                raise Exception("El ID no puede contener espacios")
            elif " " in password:
                raise Exception("No puede contener espacios la contraseña")

            else:
                return [id, password]

    def obtener_info_register(self):

        nombre = self.entry_name.get()
        nombre_sin_espacios = nombre.replace(" ", "")
        nombre_usuario = self.entry_id.get()
        correo = self.entry_correo.get()
        contrasenia = self.entry_password.get()
        v_contrasenia = self.entry_confirm_password.get()
        test_nombre_sin_espacios = nombre_sin_espacios.isalpha()
        test_correo = ("@" in correo)
        if test_nombre_sin_espacios is False:
            raise Exception("No ingresaste bien el nombre")
        elif test_correo is False:
            raise Exception("No ingresaste bien el correo")
        elif " " in contrasenia:
            raise Exception("La contraseña no contiene espacios")
        elif " " in nombre_usuario:
            raise Exception("El nombre de usuario es sin espacios")
        elif v_contrasenia != contrasenia:
            raise Exception("La verificación de contraseña no es correcta")
        else:
            return [nombre, nombre_usuario, correo, contrasenia]


    def obtener_info_change_password(self):
            old_password = self.entry_old_password.get()
            new_password = self.entry_password.get()
            if " " in old_password:
                raise Exception("Las contraseñas no pueden contener espacios")
            elif " " in new_password:
                raise Exception("Las contraseñas  no pueden contener espacios")
            else:
                return [old_password, new_password]

    def obtener_info_delete_account(self):
            password = self.entry_old_password.get()
            if " " in password:
                raise Exception("Las contraseña no pueden contener espacios")
            else:
                return password
    def desplegar_ventana_principal_window_register(self):
        self.ventana_user_register.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")

    def desplegar_ventana_principal_ventana_log_out(self):
        self.ventana_log_out.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")
    def desplegar_ventana_principal_change_password(self):
        self.ventana_change_password.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")

    def desplegar_ventana_principal_delete_account(self):
        self.ventana_delete_account.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")

    def desplegar_ventana_principal_create_window_my_project(self):
        self.ventana_my_project.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")

    def desplegar_ventana_principal_create_window_delete_risk(self):
        self.ventana_delete_risk.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")



    # CREACION DE VENTANAS
    def create_principal_window(self, controller, username=""):
        self.principal_window = PrincipalWindow()
        self.load_images()
        self.principal_window.ventana.iconbitmap("imagenes/logo.ico")
        self.principal_window.ventana.title("Algordanza Colombia")
        self.principal_window.ventana.geometry("1080x720")
        self.principal_window.ventana.resizable(False, False)
        self.principal_window.ventana.title(
            "Analisis de Riesgos en Metodologías agiles en Desarrollo de Software " + username)
        self.principal_window.ventana.config(background="#220660")
        self.principal_window.ventana.maxsize(1080,720)

        self.principal_window.title_frame = tk.Frame(self.principal_window.ventana)
        self.principal_window.title_frame.config(background="#220660")
        self.principal_window.frame_empty_1 = tk.Label(self.principal_window.title_frame,
                                                       text="                            ", background="#220660")
        self.principal_window.frame_empty_2 = tk.Label(self.principal_window.title_frame,
                                                       text="                          ", background="#220660")

        self.principal_window.title_frame.grid(row=0, column=0)
        self.principal_window.frame_empty_1.grid(row=0, column=0)
        self.principal_window.frame_empty_2.grid(row=0, column=2)

        self.principal_window.buttons_frame = tk.Frame(self.principal_window.ventana)
        self.principal_window.buttons_frame.config(background="#220660", borderwidth=0)
        self.principal_window.buttons_frame.grid(row=1, column=0)
        self.principal_window.frame_empty_3 = tk.Label(self.principal_window.buttons_frame,
                                                       text="                                                                         ",
                                                       background="#220660")
        self.principal_window.frame_empty_4 = tk.Label(self.principal_window.buttons_frame,
                                                       text="                                                                          ",
                                                       background="#220660")
        self.principal_window.frame_empty_3.grid(row=0, column=0)
        self.principal_window.frame_empty_4.grid(row=0, column=4)

        self.principal_window.title = tk.Label(self.principal_window.title_frame)
        self.principal_window.title.config(font=("Candara", 48), fg="white", image=self.logo, background="#220660")
        self.principal_window.title.grid(row=0, column=1)

        self.principal_window.button_Register = tk.Button(self.principal_window.buttons_frame, borderwidth=0,
                                                          image=self.user_register, background="#220660",
                                                          command=controller.create_window_user_register)
        self.principal_window.button_Register.grid(row=0, column=1)

        self.principal_window.button_Register_order = tk.Button(self.principal_window.buttons_frame, borderwidth=0,
                                                                image=self.sesion_start, background="#220660",
                                                                command=controller.create_window_order)
        self.principal_window.button_Register_order.grid(row=0, column=2)

        self.principal_window.ventana.mainloop()

    def create_window_register(self, controller):
        self.principal_window.ventana.withdraw()
        self.ventana_user_register = tk.Toplevel()
        self.ventana_user_register.protocol("WM_DELETE_WINDOW",self.desplegar_ventana_principal_window_register)
        self.ventana_user_register.iconbitmap("imagenes/logo.ico")
        self.ventana_user_register.geometry("1080x900")
        self.ventana_user_register.resizable(False, False)
        self.ventana_user_register.title("Registrar Cliente ")
        self.ventana_user_register.config(background="#220660")
        self.ventana_user_register.maxsize(1080, 900)
        self.ventana_user_register.state("zoomed")

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_title_frame.config(background="")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                  ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                              ",
                                                            background="#220660")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_buttons_frame.config(background="#220660", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                           ", background="#220660")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title = tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo_pequeno,
                                                background="#220660")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.label_name = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_name, borderwidth=0,
                                   background="#220660")
        self.label_name.grid(row=0, column=1)
        self.entry_name = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="#220660",
                                   background="white", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_name.grid(row=0, column=2)

        self.label_id = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_username, borderwidth=0,
                                 background="#220660")
        self.label_id.grid(row=1, column=1)
        self.entry_id = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="#220660",
                                 background="white", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_id.grid(row=1, column=2)

        self.label_correo = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_mail, borderwidth=0,
                                     background="#220660")
        self.label_correo.grid(row=2, column=1)
        self.entry_correo = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="#220660",
                                     background="white", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_correo.grid(row=2, column=2)

        self.label_password = tk.Label(self.ventana_user_register_buttons_frame, image=self.small_register_password,
                                       borderwidth=0,
                                       background="#220660")
        self.label_password.grid(row=3, column=1)
        self.entry_password = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25),
                                       fg="#220660",
                                       background="white", justify="center", bd=4, width=35, borderwidth=0, show="*")
        self.entry_password.grid(row=3, column=2)

        self.label_confirm_password = tk.Label(self.ventana_user_register_buttons_frame, image=self.verify_password,
                                       borderwidth=0,
                                       background="#220660")
        self.label_confirm_password.grid(row=4, column=1)
        self.entry_confirm_password = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25),
                                       fg="#220660",
                                       background="white", justify="center", bd=4, width=35, borderwidth=0, show="*")
        self.entry_confirm_password.grid(row=4, column=2)

        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="#220660", command=self.volver_menu)
        self.button_final_register = tk.Button(self.ventana_user_register_buttons_frame, image=self.user_register,
                                               borderwidth=0,
                                               background="#220660", command=controller.getinforegister)
        self.button_back.grid(row=5, column=1)
        self.button_final_register.grid(row=5, column=2)

        self.ventana_user_register.mainloop()
    def create_window_order(self, controller):
        self.principal_window.ventana.withdraw()
        self.ventana_user_register = tk.Toplevel()
        self.ventana_user_register.protocol("WM_DELETE_WINDOW", self.desplegar_ventana_principal_window_register)
        self.ventana_user_register.iconbitmap("imagenes/logo.ico")
        self.ventana_user_register.geometry("1080x900")
        self.ventana_user_register.resizable(False, False)
        self.ventana_user_register.title("Iniciar Sesión")
        self.ventana_user_register.config(background="#220660")
        self.ventana_user_register.maxsize(1080, 900)
        self.ventana_user_register.state("zoomed")

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_title_frame.config(background="#220660")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                  ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                              ",
                                                            background="#220660")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_buttons_frame.config(background="#220660", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                           ", background="#220660")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title = tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo, background="#220660")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.label_id = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_username, borderwidth=0,
                                 background="#220660")
        self.label_id.grid(row=0, column=1)
        self.entry_id = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="#220660",
                                 background="white", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_id.grid(row=0, column=2)

        self.label_password = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_password,
                                       borderwidth=0,
                                       background="#220660")
        self.label_password.grid(row=1, column=1)
        self.entry_password = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25),
                                       fg="#220660",
                                       background="white", justify="center", bd=4, width=35, borderwidth=0, show="*")
        self.entry_password.grid(row=1, column=2)

        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="#220660", command=self.volver_menu)
        self.button_final_order = tk.Button(self.ventana_user_register_buttons_frame, image=self.sesion_start,
                                            borderwidth=0,
                                            background="#220660", command=controller.log_in)
        self.button_back.grid(row=4, column=1)
        self.button_final_order.grid(row=4, column=2)

        self.ventana_user_register.mainloop()

    def create_window_log_out(self, controller, username=""):
        self.principal_window.ventana.withdraw()
        self.ventana_log_out = tk.Toplevel()
        self.ventana_log_out.protocol("WM_DELETE_WINDOW",self.desplegar_ventana_principal_ventana_log_out)
        self.ventana_log_out.iconbitmap("imagenes/logo.ico")
        self.ventana_log_out.geometry("1080x900")
        self.ventana_log_out.resizable(False, False)
        self.ventana_log_out.title("ADRMA usuario: " + username)
        self.ventana_log_out.config(background="#220660")
        self.ventana_log_out.maxsize(1080, 900)
        self.ventana_log_out.state("zoomed")

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_log_out)
        self.ventana_user_register_title_frame.config(background="#220660")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                                                                            ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                              ",
                                                            background="#220660")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_log_out)
        self.ventana_user_register_buttons_frame.config(background="#220660", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                           ", background="#220660")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title = tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo_pequeno, background="#220660")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.button_final_register = tk.Button(self.ventana_user_register_buttons_frame, image=self.log_out,
                                               borderwidth=0,
                                               background="#220660", command=controller.log_out)
        self.button_change_password = tk.Button(self.ventana_user_register_buttons_frame, image=self.change_password,
                                                borderwidth=0,
                                                background="#220660", command=controller.change_password)
        self.button_my_project = tk.Button(self.ventana_user_register_buttons_frame, image=self.my_project,
                                                borderwidth=0,
                                                background="#220660", command=controller.my_project)
        self.button_delete_account = tk.Button(self.ventana_user_register_buttons_frame, image=self.delete_account,
                                               borderwidth=0,
                                               background="#220660", command=controller.delete_account)
        self.button_delete_account.grid(row=5, column=2)
        self.button_change_password.grid(row=3, column=2)
        self.button_my_project.grid(row=2,column=2)
        self.button_final_register.grid(row=4, column=2)
        self.button_delete_account.grid(row=5, column=2)
        self.labelbutton = tk.Label(self.ventana_user_register_buttons_frame,
                                    text="                                                                                              ",
                                    background="#220660")
        self.labelbutton.grid(row=4, column=1)

        self.ventana_log_out.mainloop()

    def create_window_change_password(self, controller, username=""):
        self.ventana_log_out.withdraw()
        self.ventana_change_password = tk.Toplevel()
        self.ventana_change_password.protocol("WM_DELETE_WINDOW",self.desplegar_ventana_principal_change_password)
        self.ventana_change_password.iconbitmap("imagenes/logo.ico")
        self.ventana_change_password.geometry("1080x900")
        self.ventana_change_password.resizable(False, False)
        self.ventana_change_password.title("Usuario: " + username + " -> Cambio de contraseña")
        self.ventana_change_password.config(background="#220660")
        self.ventana_change_password.maxsize(1080, 900)
        self.ventana_change_password.state("zoomed")

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_change_password)
        self.ventana_user_register_title_frame.config(background="#220660")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                  ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                              ",
                                                            background="#220660")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_change_password)
        self.ventana_user_register_buttons_frame.config(background="#220660", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                           ", background="#220660")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title = tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo, background="#220660")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.label_id = tk.Label(self.ventana_user_register_buttons_frame, image=self.actual_password, borderwidth=0,
                                 background="#220660")
        self.label_id.grid(row=0, column=1)
        self.entry_old_password = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25),
                                           fg="#220660", background="white", justify="center", bd=4, width=35,
                                           borderwidth=0, show="*")
        self.entry_old_password.grid(row=0, column=2)

        self.label_password = tk.Label(self.ventana_user_register_buttons_frame, image=self.new_password, borderwidth=0,
                                       background="#220660")
        self.label_password.grid(row=1, column=1)
        self.entry_password = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25),
                                       fg="#220660",
                                       background="white", justify="center", bd=4, width=35, borderwidth=0,show="*" )
        self.entry_password.grid(row=1, column=2)

        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="#220660", command=self.back_create_window_log_out)
        self.button_final_order = tk.Button(self.ventana_user_register_buttons_frame, image=self.change_password,
                                            borderwidth=0,
                                            background="#220660", command=controller.getinfochangepassword)
        self.button_back.grid(row=4, column=1)
        self.button_final_order.grid(row=4, column=2)

        self.ventana_change_password.mainloop()

    def create_window_delete_account(self, controller, username=""):
        self.ventana_log_out.withdraw()
        self.ventana_delete_account = tk.Toplevel()
        self.ventana_delete_account.protocol("WM_DELETE_WINDOW",self.desplegar_ventana_principal_delete_account)
        self.ventana_delete_account.iconbitmap("imagenes/logo.ico")
        self.ventana_delete_account.geometry("1080x900")
        self.ventana_delete_account.resizable(False, False)
        self.ventana_delete_account.title("Usuario: " + username + " -> Eliminación de cuenta")
        self.ventana_delete_account.config(background="#220660")
        self.ventana_delete_account.maxsize(1080, 900)
        self.ventana_delete_account.state("zoomed")

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_delete_account)
        self.ventana_user_register_title_frame.config(background="#220660")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                  ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                              ",
                                                            background="#220660")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_delete_account)
        self.ventana_user_register_buttons_frame.config(background="#220660", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                           ", background="#220660")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ",
                                                            background="#220660")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title = tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo, background="#220660")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.label_id = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_password, borderwidth=0,
                                 background="#220660")
        self.label_id.grid(row=0, column=1)
        self.entry_old_password = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25),
                                           fg="#220660", background="white", justify="center", bd=4, width=35,
                                           borderwidth=0,show="*" )
        self.entry_old_password.grid(row=0, column=2)

        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="#220660", command=self.back_create_window_log_out_delete_account)
        self.button_final_order = tk.Button(self.ventana_user_register_buttons_frame, image=self.delete_account,
                                            borderwidth=0,
                                            background="#220660", command=controller.getinfodelete_account)
        self.button_back.grid(row=4, column=1)
        self.button_final_order.grid(row=4, column=2)

        self.ventana_delete_account.mainloop()

    def create_window_my_project(self, controller, username=""):
        self.principal_window.ventana.withdraw()
        self.ventana_my_project = tk.Toplevel()
        self.ventana_my_project.protocol("WM_DELETE_WINDOW",self.desplegar_ventana_principal_create_window_my_project)
        self.ventana_my_project.iconbitmap("imagenes/logo.ico")
        self.ventana_my_project.geometry("1080x900")
        self.ventana_my_project.resizable(False, False)
        self.ventana_my_project.title("ADRMA usuario: " + username)
        self.ventana_my_project.config(background="#220660")
        self.ventana_my_project.maxsize(1080, 900)
        self.ventana_my_project.state("zoomed")

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_my_project)
        self.ventana_user_register_title_frame.config(background="#220660")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame,
                                                                text="                                                                                            ",
                                                                background="#220660")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                                text="                                              ",
                                                                background="#220660")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_my_project)
        self.ventana_user_register_buttons_frame.config(background="#220660", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                                text="                           ",
                                                                background="#220660")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                                text="                                                       ",
                                                                background="#220660")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title = tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo_pequeno,
                                                    background="#220660")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.button_see_taxonomy = tk.Button(self.ventana_user_register_buttons_frame, image=self.see_taxonomy,
                                                   borderwidth=0,
                                                   background="#220660", command=controller.open_taxonomy)
        self.button_delete_risk = tk.Button(self.ventana_user_register_buttons_frame, image=self.delete_risk,
                                             borderwidth=0,
                                             background="#220660", command=controller.create_window_delete_risk)
        self.button_restart_tax = tk.Button(self.ventana_user_register_buttons_frame, image=self.restart_taxonomy,
                                            borderwidth=0,
                                            background="#220660", command=controller.restart_my_tax)

        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="#220660", command=self.back_my_proyect_window_log_out)

        self.button_see_taxonomy.grid(row=2, column=2)
        self.button_delete_risk.grid(row=3,column=2)
        self.button_restart_tax.grid(row=4,column=2)
        self.button_back.grid(row=5, column=2)
        self.labelbutton = tk.Label(self.ventana_user_register_buttons_frame,
                                        text="                                                                                              ",
                                        background="#220660")
        self.labelbutton.grid(row=4, column=1)

        self.ventana_my_project.mainloop()


    def create_window_delete_risk(self,controller, username="", Taxonomy=None):
        if Taxonomy is None:
            Taxonomy = []
        self.ventana_my_project.withdraw()
        self.ventana_delete_risk = tk.Toplevel()
        self.ventana_delete_risk.protocol("WM_DELETE_WINDOW",self.desplegar_ventana_principal_create_window_delete_risk)
        self.ventana_delete_risk.iconbitmap("imagenes/logo.ico")
        self.ventana_delete_risk.geometry("1080x900")
        self.ventana_delete_risk.resizable(False, False)
        self.ventana_delete_risk.title("ADRMA usuario: " + username)
        self.ventana_delete_risk.config(background="#220660")
        self.ventana_delete_risk.maxsize(1080, 900)
        self.ventana_delete_risk.state("zoomed")

        self.ventana_user_register_title_frame_delete_risk = tk.Frame(self.ventana_delete_risk)
        self.ventana_user_register_title_frame_delete_risk.config(background="#220660")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame_delete_risk,
                                                                text="                                                                                                               ",
                                                                background="#220660")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame_delete_risk,
                                                                text="                                                           ",
                                                                background="#220660")

        self.ventana_user_register_title_frame_delete_risk.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_delete_risk)
        self.ventana_user_register_buttons_frame.config(background="#220660", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                                text="                                                                  ",
                                                                background="#220660")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                                text="         ",
                                                                background="#220660")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title = tk.Label(self.ventana_user_register_title_frame_delete_risk)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo_pequeno,
                                                    background="#220660")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.label_title_delete_tax = tk.Label(self.ventana_user_register_buttons_frame,text=" Elige el riesgo que quieres eliminar de tu taxonomia : \n", font=("Candara",24),
                                                fg="white",
                                                 background="#220660")
        self.taxonomy = tk.StringVar()
        self.taxonomy.set(Taxonomy[0])
        self.option_risk_menu = tk.OptionMenu(self.ventana_user_register_buttons_frame,self.taxonomy,*Taxonomy)
        self.option_risk_menu.config(font=("Candara",24),fg="white",background="#220660",highlightbackground="#220660",highlightcolor="white")

        self.option_risk_menu.grid(row=3,column=2)

        self.button_delete_my_risk = tk.Button(self.ventana_user_register_buttons_frame, image=self.delete_risk, borderwidth=0,
                                     background="#220660", command=controller.delete_my_risk)
        self.button_delete_my_risk.grid(row=4,column=2)


        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                         background="#220660", command=self.volver_my_project)

        self.label_title_delete_tax.grid(row=2, column=2)
        self.button_back.grid(row=5, column=2)

        self.ventana_my_project.mainloop()

    def volver_my_project(self):
            self.ventana_delete_risk.destroy()
            self.ventana_my_project.iconify()
            self.ventana_my_project.state("zoomed")
    def get_info_delete_risk(self):
        info = self.taxonomy.get()
        return info
    def question_restart_taxonomy(self):
        respuesta = tk.messagebox.askquestion("Restablecer Taxonomía","¿Estas seguro que quieres reiniciar la taxonomia?")
        return respuesta



