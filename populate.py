from scripts.db_impuesto import db_vencimiento, db_impuesto, db_multa
from scripts.db_direccion import db_parroquia
from scripts.db_tipos import db_tipo_contribuyente, db_tipo_actividad

try:
    db_tipo_contribuyente()
    db_tipo_actividad()
    db_vencimiento()
    db_impuesto()
    db_multa()
    db_parroquia()
    print('--- Script DB finalizado ----')
except BaseException as error:
    print('Ha ocurrido un error: {}'.format(error))
