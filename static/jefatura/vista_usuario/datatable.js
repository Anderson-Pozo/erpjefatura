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
                'action': 'search_data',
                // 'usuario': '1234567891001'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            {"data": "ruc"},
            {"data": "nombre_contribuyente"},
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
                    let buttons = '<a class="btn btn-datatable btn-icon btn-outline-secondary mr-2"' +
                        ' onclick="">' +
                        '<i class="fas fa-funnel-dollar"></i>' +
                        '</a>';
                    return buttons;
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (row.estado) {
                        return '<span class="badge badge-success">Activo</span>';
                    } else {
                        return '<span class="badge badge-danger">Suspendido</span>';
                    }
                }
            }
        ],
        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
}

$(document).ready(() => lista_vista_usuario());
