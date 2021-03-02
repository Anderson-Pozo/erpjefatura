from scripts.db_impuesto import db_vencimiento, db_impuesto, db_multa

try:
    db_vencimiento()
    db_impuesto()
    db_multa
    print('Script DB completado')
except BaseException as error:
    print('Ha ocurrido un error: {}'.format(error))
