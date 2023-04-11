from UItkinter import *
from controller import *


if __name__ == '__main__':

    interfaz = UI()
    modelo= Program()
    controller = Controller(interfaz,modelo)
    controller.start()







