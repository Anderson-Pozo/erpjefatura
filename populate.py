from scripts.db_impuesto import db_vencimiento

try:
    db_vencimiento()
    print('Script DB completado')
except BaseException as error:
    print('Ha ocurrido un error: {}'.format(error))
