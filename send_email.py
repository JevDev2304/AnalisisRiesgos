import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_correo( destinatario, asunto, mensaje, contraseña ="Jevo2304*" ,remitente="analisisriesgosmetodologias@outlook.com"):
    # Obtener el dominio del remitente y del destinatario
    dominio_remitente = remitente.split('@')[1].lower()
    dominio_destinatario = destinatario.split('@')[1].lower()

    # Configurar los detalles del servidor de correo saliente según el dominio del remitente
    if dominio_remitente == 'gmail.com':
        servidor_smtp = 'smtp.gmail.com'
        puerto_smtp = 587
    elif dominio_remitente == 'outlook.com' or dominio_remitente == 'hotmail.com':
        servidor_smtp = 'smtp-mail.outlook.com'
        puerto_smtp = 587
    else:
        raise ValueError('No se admite el dominio de correo electrónico del remitente.')

    # Crear conexión segura con el servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, contraseña)

    # Crear el mensaje del correo electrónico
    mensaje_correo = MIMEMultipart()
    mensaje_correo['From'] = remitente
    mensaje_correo['To'] = destinatario
    mensaje_correo['Subject'] = asunto
    mensaje_correo.attach(MIMEText(mensaje, 'plain', 'utf-8'))

    # Enviar el correo electrónico
    servidor.send_message(mensaje_correo)

    # Cerrar la conexión con el servidor SMTP
    servidor.quit()

# Ejemplo de uso
