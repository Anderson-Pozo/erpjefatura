import threading

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
from django.conf import settings


def send_mail_fun(destinatario, tipo, data):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        print(mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD))
        print('Conectado..')

        message = MIMEMultipart()
        message['From'] = settings.EMAIL_HOST_USER
        message['To'] = destinatario
        message['Subject'] = 'Jefatura de Rentas GAD Municipal Huaca'

        if tipo == 1:
            context = render_to_string('administrador/email_temp/bienvenida.html', data)
        elif tipo == 2:
            context = render_to_string('administrador/email_temp/notificacion.html', data)

        message.attach(MIMEText(context, 'html'))

        mailServer.sendmail(
            settings.EMAIL_HOST_USER,
            destinatario,
            message.as_string()
        )
        print('Correo enviado correctamente')
    except Exception as error:
        print(error)


def send_mail_thread(arg1, arg2, arg3):
    thread = threading.Thread(target=send_mail_fun, args=(arg1, arg2, arg3))
    thread.start()
