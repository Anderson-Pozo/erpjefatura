function format(d) {
    return '<table cellpadding="5" cellspacing="0" style="padding-left:50px; border: hidden">' +
        '<tr>' +
        '<td>Descripción del tramite:</td>' +
        '<td>' + d.descripcion_tramite + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>valor de la compra y venta:</td>' +
        '<td>' + d.valor_compra_venta + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Impuesto Alcabalas:</td>' +
        '<td>' + d.impuesto_alcabalas + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Alcabalas Provinciales:</td>' +
        '<td>' + d.alcabalas_provinciales + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Fondos Escolares:</td>' +
        '<td>' + d.fondos_escolares + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>fondo de prevención de riesgos:</td>' +
        '<td>' + d.fondos_prevencion_riesgos + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Agua Potable:</td>' +
        '<td>' + d.agua_potable + '</td>' +
        '</tr>' +
        '</table>';
}

function lista_alcabala() {
    let table = $('#tableAlcabala').DataTable({
        language: {
            'url': 'https://raw.githubusercontent.com/Jhon-Paillacho/ERP-estaticos/main/language.json'
        },
        dom: "<'row'<'col-sm-12 col-md-6'B><'col-sm-12 col-md-6'f>>" +
            "<'row'<'col-sm-12'tr>>" +
            "<'row'<'col-sm-12 col-md-5'li><'col-sm-12 col-md-7'p>>",
        buttons: [
            {
                extend: 'excelHtml5',
                text: 'Exportar Excel <i class="fas fa-file-excel"></i>',
                titleAttr: 'Excel',
                className: 'btn btn-green btn-flat btn-xs'
            },
            {
                extend: 'pdfHtml5',
                text: 'Exportar PDF <i class="fas fa-file-pdf"></i>',
                titleAttr: 'PDF',
                className: 'btn btn-red btn-flat btn-xs'
            },
            {
                extend: 'print',
                text: 'Imprimir <i class="fas fa-print"></i>',
                titleAttr: 'Imprimir',
                className: 'btn btn-teal btn-flat btn-xs'
            },
            // 'excel', 'pdf', 'print'
        ],
        responsive: true,
        autoWidth: true,
        destroy: true,
        deferRender: true,
        ordering: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": '',
                // render: (data, type, row) =>{
                //     let datos = new Object(data);
                //     // console.log(datos);
                //     // return `<button onclick="show_childs( ${datos})"></buttonon>`;
                //     // return '<button onclick="show_childs(\'' + datos +'\')">aC</button>';
                // }
            },
            {"data": "fecha"},
            {"data": "predio"},
            {"data": "comprador"},
            {"data": "vendedor"},
        ],

        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
    $('#tableAlcabala tbody').on('click', 'td.details-control',
        function () {
            let tr = $(this).closest('tr');
            let row = table.row(tr);

            if (row.child.isShown()) {
                row.child.hide();
                tr.removeClass('shown');
            } else {
                row.child(format(row.data())).show();
                // console.log(row.data());
                tr.addClass('shown');
            }
        });
}

function show_childs(variable) {
    console.log(JSON.parse(variable));

}

// $(document).ready(function () {
//     lista_alcabala();
// })

$(document).ready(() => lista_alcabala());