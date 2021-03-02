from scripts.db_impuesto import db_vencimiento, db_impuesto

try:
    # db_vencimiento()
    db_impuesto()
    print('Script DB completado')
except BaseException as error:
    print('Ha ocurrido un error: {}'.format(error))
