$(function () {
    // Plusvalia
    let i_fecha_escritura = $('input[name="fecha_escritura"]');
    let i_fecha_tramite = $('input[name="fecha_tramite"]');
    let i_precio_venta = $('input[name="precio_venta"]');
    let i_precio_adquisicion = $('input[name="precio_adquisicion"]');
    let i_diferencia_bruta = $('input[name="diferencia_bruta"]');
    let i_rebaja_mejoras = $('input[name="rebaja_mejoras"]');
    let i_diferencia_neta = $('input[name="diferencia_neta"]');
    let i_tenencia = $('input[name="tenencia"]');
    let i_base_rebajar_moneda = $('input[name="base_rebajar_moneda"]');
    let i_rebaja_desvalorizacion = $('input[name="rebaja_desvalorizacion"]');
    let i_utilidad_imponible = $('input[name="utilidad_imponible"]');
    let i_totalp = $('#totalp');

    function sumap() {

        var val_fecha_escritura = moment(i_fecha_escritura.val());
        var val_fecha_tramite = moment(i_fecha_tramite.val());
        console.log(val_fecha_escritura);
        console.log(val_fecha_tramite);

        var anios = val_fecha_tramite.diff(val_fecha_escritura, "years")
        $("#res").text(anios)

        let val_precio_venta = parseFloat(i_precio_venta.val());
        let val_precio_adquisicion = parseFloat(i_precio_adquisicion.val());
        // let val_diferencia_bruta = parseFloat(i_diferencia_bruta.val());

//1 diferencia bruta
        let dif_bruta = val_precio_venta - val_precio_adquisicion
        i_diferencia_bruta.val(parseFloat(dif_bruta.toFixed(2)));

//2 diferencia neta
        let dif_neta = dif_bruta
        i_diferencia_neta.val(parseFloat(dif_neta.toFixed(2)));

//3 tenencia
        let val_diferencia_neta = parseFloat(i_diferencia_neta.val());
        // let val_tenencia = parseFloat(i_tenencia.val());
        let dif_tenencia = (val_diferencia_neta * 0.05) * anios
        console.log(parseInt(anios));
        i_tenencia.val(parseFloat(dif_tenencia.toFixed((2))));

//4 Base Rebaja Moneda
        let dif_rebaja_moneda = dif_neta - dif_tenencia
        i_base_rebajar_moneda.val(parseFloat(dif_rebaja_moneda.toFixed(2)));

//5  Rebaja desvalorizacion Moneda
        let val_base_rebajar_moneda = parseFloat(i_base_rebajar_moneda.val());
        i_rebaja_desvalorizacion.val(val_base_rebajar_moneda);
        let val_rebaja_desvalorizacion = parseFloat(i_rebaja_desvalorizacion.val());


        let val_rebaja_mejoras = parseFloat(i_rebaja_mejoras.val());
        let val_utilidad_imponible = parseFloat(i_utilidad_imponible.val());

        let totalp = ((val_rebaja_desvalorizacion * 0.05) + val_rebaja_mejoras +
            val_utilidad_imponible).toFixed(2);
        i_totalp.text(parseFloat(totalp));
    }

    sumap();

    i_precio_venta.on('change', () => {
        sumap();
    });

    i_precio_adquisicion.on('change', () => {
        sumap();
    })

    i_diferencia_bruta.on('change', () => {
        sumap();
    })

    i_rebaja_mejoras.on('change', () => {
        sumap();
    })

    i_diferencia_neta.on('change', () => {
        sumap();
    })

    i_tenencia.on('change', () => {
        sumap();
    })
    i_base_rebajar_moneda.on('change', () => {
        sumap();
    })

    i_rebaja_desvalorizacion.on('change', () => {
        sumap();
    })

    i_utilidad_imponible.on('change', () => {
        sumap();
    })
})(jQuery);