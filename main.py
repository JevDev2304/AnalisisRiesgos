from UItkinter import *
from controller import *


if __name__ == '__main__':

    interfaz = UI()
    modelo = Program()
    diccionario_json = modelo.read_json()
    modelo.load_json(diccionario_json)
    controller = Controller(interfaz,modelo)
    controller.start()
    modelo.save_json()








