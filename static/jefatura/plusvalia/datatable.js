function format(d) {
    return '<table cellpadding="5" cellspacing="0" style="padding-left:50px; border: hidden">' +
        '<tr>' +
        '<td>Valor en la escritura:</td>' +
        '<td>' + d.precio_venta + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Precio de adquisición:</td>' +
        '<td>' + d.precio_adquisicion + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Rebaja por mejoras:</td>' +
        '<td>' + d.rebaja_mejoras + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Diferencia neta:</td>' +
        '<td>' + d.diferencia_neta + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Valor de tenencia:</td>' +
        '<td>' + d.tenencia + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Base para rebajar por Desvalorización Moneda:</td>' +
        '<td>' + d.base_rebajar_moneda + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Rebaja por Desvalorización Moneda:</td>' +
        '<td>' + d.rebaja_desvalorizacion + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Utilidad imponible:</td>' +
        '<td>' + d.utilidad_imponible + '</td>' +
        '</tr>' +
        '<td>Total:</td>' +
        '<td>' + d.total + '</td>' +
        '</tr>' +
        '</table>';
}

function lista_plusvalia() {
    let table = $('#tablePlusvalia').DataTable({
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

            {"data": "fecha_tramite"},
            {"data": "comprador"},
            {"data": "vendedor"},
            {"data": "precio_adquisicion"},
            {"data": "precio_venta"},
            {"data": "acciones"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<a class="btn btn-datatable btn-icon btn-outline-secondary mr-2"' +
                        ' onclick="window.open(\'/plusvalia/report_plusvalia/' + row.id + '/\')">' +
                        '<i class="fas fa-print"></i>' +
                        '</a>';
                    return buttons;
                }
            },
        ],

        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
    $('#tablePlusvalia tbody').on('click', 'td.details-control',
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


$(document).ready(function () {
    lista_plusvalia();
})