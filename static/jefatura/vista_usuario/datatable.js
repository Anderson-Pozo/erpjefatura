function lista_vista_usuario() {
    let table = $('#tableVistaUsuario').DataTable({
        language: {
            'url': 'https://raw.githubusercontent.com/Jhon-Paillacho/ERP-estaticos/main/language.json'
        },
        // dom: "<'row'<'col-sm-12 col-md-6'B><'col-sm-12 col-md-6'f>>" +
        //     "<'row'<'col-sm-12'tr>>" +
        //     "<'row'<'col-sm-12 col-md-5'li><'col-sm-12 col-md-7'p>>",
        // buttons: [
        //     {
        //         extend: 'excelHtml5',
        //         text: 'Exportar Excel <i class="fas fa-file-excel"></i>',
        //         titleAttr: 'Excel',
        //         className: 'btn btn-green btn-flat btn-xs'
        //     },
        //     {
        //         extend: 'pdfHtml5',
        //         text: 'Exportar PDF <i class="fas fa-file-pdf"></i>',
        //         titleAttr: 'PDF',
        //         className: 'btn btn-red btn-flat btn-xs'
        //     },
        //     {
        //         extend: 'print',
        //         text: 'Imprimir <i class="fas fa-print"></i>',
        //         titleAttr: 'Imprimir',
        //         className: 'btn btn-teal btn-flat btn-xs'
        //     },
        //     // 'excel', 'pdf', 'print'
        // ],
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
            {"data": "fecha_ultimo_pago"},
            {"data": "impuesto"},
            {"data": "interes"},
            {"data": "multa"},
            {"data": "servicios"}
        ],

        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
    $('#tableVistaUsuario tbody').on('click', 'td.details-control',
        function () {
            let tr = $(this).closest('tr');
            let row = table.row(tr);

            if (row.child.isShown()) {
                row.child.hide();
                tr.removeClass('shown');
            } else {
                row.child(format(row.data())).show();
                console.log(row.data());
                tr.addClass('shown');
            }
        });
}

$(document).ready(() => lista_vista_usuario());
