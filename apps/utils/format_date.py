from datetime import datetime


def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    hour = date.strftime('%H:%M:%S')
    messsage = "{} {}, {} {}".format(day, month, year, hour)

    return messsage


# now = datetime.now()
# print(current_date_format(now))
