from datetime import datetime


def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    hour = date.strftime('%H:%M:%S')
    messsage = "{} {}, {} {}".format(day, month, year, hour)

    return messsage


def format_month_day(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    message = "{} de {}".format(day, month)
    return message


def format_month_year(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    month = months[date.month - 1]
    year = date.year
    message = "{} - {}".format(year, month)
    return message

