function lista_catastro() {
    $('#tableCatastro').DataTable({
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
        // scrollX: true,
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
            {"data": "ruc"},
            { "data": "nombre_contribuyente"},
            {"data": "tipocontribuyente"},
            {"data": "nombre_establecimiento"},
            {"data": "total_patrimonio"},
            {"data": "exonerada"},
            {"data": "acciones"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<div class="dropdown no-caret">\n' +
                        ' <button class="btn btn-transparent-dark btn-datatable dropdown-toggle" ' +
                        'id="dropdownPeople1" type="button" data-toggle="dropdown" aria-haspopup="true" ' +
                        'aria-expanded="false"><i class="fas fa-ellipsis-v"></i></button>\n' +
                        '    <div class="dropdown-menu dropdown-menu-right animated--fade-in-up" aria-labelledby="dropdownPeople1">\n' +
                        '        <button class="dropdown-item btn-light" href="#">Suspensión</button>\n' +
                        '        <button class="dropdown-item btn-light" href="#">Exoneración</button>\n' +
                        '        <button class="dropdown-item btn-light" href="#">Renovación</button>\n' +
                        '        <button class="dropdown-item btn-light" href="#">Historial</button>\n' +
                        '    </div>\n' +
                        '</div>';
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (!row.suspendida && !row.exonerada) {
                        return '<span class="badge badge-light">Normal</span>';
                    }
                    if (row.exonerada) {
                        return '<span class="badge badge-success">Exonerada</span>';
                    }
                    if (row.suspendida) {
                        return '<span class="badge badge-danger">Suspendida</span>';
                    }

                }
            }
        ],
        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
}

$(document).ready(function () {
    lista_catastro();
})