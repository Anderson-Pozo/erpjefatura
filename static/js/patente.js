$(function () {
    let i_impuesto = $('input[name="impuesto"]');
    let i_interes = $('input[name="interes"]');
    let i_multa = $('input[name="multa"]');
    let i_serv = $('input[name="servicios_administrativos"]');
    let i_total = $('#total');

    function suma() {
        let val_impuesto = parseFloat(i_impuesto.val());
        let val_interes = parseFloat(i_interes.val());
        let val_multa = parseFloat(i_multa.val());
        let val_serv = parseFloat(i_serv.val());

        let total = val_impuesto + val_interes + val_multa + val_serv;
        i_total.text(parseFloat(total.toFixed(2)));
    }

    suma();

    i_impuesto.on('change', () => {
        suma();
    });

    i_interes.on('change', () => {
        suma();
    })

    i_multa.on('change', () => {
        suma();
    })

    i_serv.on('change', () => {
        suma();
    })

});