import tkinter as tk
from tkinter import scrolledtext, filedialog


class Notepad:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bloc de Notas")

        self.text_area = scrolledtext.ScrolledText(self.window, width=100, height=30)
        self.text_area.pack()

        self.menu_bar = tk.Menu(self.window)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Nuevo", command=self.nuevo_archivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.window.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        self.window.config(menu=self.menu_bar)

        self.window.mainloop()

    def nuevo_archivo(self):
        self.text_area.delete('1.0', tk.END)

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', file.read())

    def guardar_archivo(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get('1.0', tk.END))

Notepad()