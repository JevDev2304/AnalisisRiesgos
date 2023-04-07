from exceptions import *
import re as re
from datetime import *


def validar_correo(correo):
    # Expresión regular para validar el formato del correo electrónico
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Verificar si el correo cumple con el patrón de la expresión regular
    try:
        if re.match(patron, correo):
            return True
        else:
            raise CorreoNoEsValido("El correo no es valido", "El correo tiene caracteres no validos", "Sugerencias",
                                   "Debe tener @ y algunos caracteres especiales no estan permitidos")
    except CorreoNoEsValido as cnv:
        return cnv

def validar_fecha(fecha_string):
    try:
        fecha = datetime.strptime(fecha_string, '%Y-%m-%d %H:%M:%S')
        return fecha
    except ValueError as ve:
        raise FechaMalIngresada("Fecha mal ingresada", "El formato de fecha no esta bien escrito","Sugerencias","el formato es Día/Mes/Año")