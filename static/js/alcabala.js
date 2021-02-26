$(function () {

    let i_valor_compra_venta = $('input[name="valor_compra_venta"]');
    let i_impuesto_alcabalas = $('input[name="impuesto_alcabalas"]');
    let i_alcabalas_provinciales = $('input[name="alcabalas_provinciales"]');
    let i_fondos_escolares = $('input[name="fondos_escolares"]');
    let i_fondos_prevencion_riesgos = $('input[name="fondos_prevencion_riesgos"]');
    let i_agua_potable = $('input[name="agua_potable"]');
    let i_total = $('#total');

    function suma() {
        let val_valor_compra_venta = parseFloat(i_valor_compra_venta.val());

        let impuesto_alcabala = val_valor_compra_venta * 0.01
        i_impuesto_alcabalas.val(parseFloat(impuesto_alcabala.toFixed(2)));

        let impuesto_provincial = val_valor_compra_venta * 0.00001
        i_alcabalas_provinciales.val(parseFloat(impuesto_provincial.toFixed(2)));

        let impuesto_escolar = val_valor_compra_venta * 0.0001
        i_fondos_escolares.val(parseFloat(impuesto_escolar.toFixed(2)));

        let val_impuesto_alcabalas = parseFloat(i_impuesto_alcabalas.val());
        let val_alcabalas_provinciales = parseFloat(i_alcabalas_provinciales.val());
        let val_fondos_escolares = parseFloat(i_fondos_escolares.val());
        let val_fondos_prevencion_riesgos = parseFloat(i_fondos_prevencion_riesgos.val());
        let val_agua_potable = parseFloat(i_agua_potable.val());

        let total = val_impuesto_alcabalas + val_alcabalas_provinciales
            + val_fondos_escolares + val_fondos_prevencion_riesgos + val_agua_potable;

        console.log(total);

        i_total.text(parseFloat(total.toFixed(2)));
    }

    suma();

    i_valor_compra_venta.on('change', () => {
        suma();
    });

    i_impuesto_alcabalas.on('change', () => {
        suma();
    })

    i_alcabalas_provinciales.on('change', () => {
        suma();
    })

    i_fondos_escolares.on('change', () => {
        suma();
    })
    i_fondos_prevencion_riesgos.on('change', () => {
        suma();
    })

    i_agua_potable.on('change', () => {
        suma();
    })

})(jQuery);