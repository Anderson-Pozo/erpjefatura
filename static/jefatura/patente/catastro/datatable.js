$(() => {
    let tbl_catastro = $('#tableCatastro').DataTable({
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
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
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
                    return `<div class="dropdown no-caret">
                        <button class="btn btn-transparent-dark btn-datatable dropdown-toggle"
                        id="dropdownPeople1" type="button" data-toggle="dropdown" aria-haspopup="true"
                        aria-expanded="false"><i class="fas fa-ellipsis-v"></i></button>
                        <div class="dropdown-menu dropdown-menu-right animated--fade-in-up" aria-labelledby="dropdownPeople1">
                                <a class="dropdown-item btn-light" href="/patente/actualizar_declaracion/${row.id}">Suspender</a>
                                <a class="dropdown-item btn-light" href="/patente/actualizar_declaracion/${row.id}">Exonerar</a>
                                <a class="dropdown-item btn-light" href="/patente/actualizar_declaracion/${row.id}">Renovar</a>
                                <a rel="details" class="dropdown-item btn-light" href="#">Historial</a>
                            </div>
                        </div>`
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: true,
                render: function (data, type, row) {
                    return row.estado
                }
            }
        ],
    });

    $('#tableCatastro tbody')
        .on('click', 'a[rel="details"]', function () {
            let tr = tbl_catastro.cell($(this).closest('td, li')).index();
            let data = tbl_catastro.row(tr.row).data();
            console.log(data);

            // $('#tblDet').DataTable({
            //     responsive: true,
            //     autoWidth: false,
            //     destroy: true,
            //     deferRender: true,
            //     //data: data.det,
            //     ajax: {
            //         url: window.location.pathname,
            //         type: 'POST',
            //         data: {
            //             'action': 'search_details',
            //             'id': data.id
            //         },
            //         dataSrc: ""
            //     },
            //     columns: [
            //         {"data": "prod.name"},
            //         {"data": "prod.cat.name"},
            //         {"data": "price"},
            //         {"data": "cant"},
            //         {"data": "subtotal"},
            //     ],
            //     columnDefs: [
            //         {
            //             targets: [-1, -3],
            //             class: 'text-center',
            //             render: function (data, type, row) {
            //                 return '$' + parseFloat(data).toFixed(2);
            //             }
            //         },
            //         {
            //             targets: [-2],
            //             class: 'text-center',
            //             render: function (data, type, row) {
            //                 return data;
            //             }
            //         },
            //     ],
            //     initComplete: function (settings, json) {
            //
            //     }
            // });
            $('#myModelDet').modal('show');
        })
})


// function lista_catastro() {
//
// }
//
// $(document).ready(function () {
//     lista_catastro();
// })