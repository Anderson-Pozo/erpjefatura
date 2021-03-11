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
            {"data": "estado_pago"},
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
                    return `<div class="row"></div><div class="dropdown no-caret">
                        <button class="btn btn-transparent-dark btn-datatable dropdown-toggle"
                        id="dropdownPeople1" type="button" data-toggle="dropdown" aria-haspopup="true"
                        aria-expanded="false"><i class="fas fa-ellipsis-v"></i></button>
                        <div class="dropdown-menu dropdown-menu-right animated--fade-in-up" aria-labelledby="dropdownPeople1">
                                <a class="dropdown-item btn-light" href="/patente/especie_renovacion/${row.id}">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-sync-alt"></i>
                                    </div>
                                    Renovar
                                </a>
                                <a class="dropdown-item btn-light" href="/patente/report_declaracion/${row.id}" target="_blank">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-print"></i>
                                    </div>
                                    Declaración
                                </a>
                                <a rel="details" class="dropdown-item btn-light">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-funnel-dollar"></i>
                                    </div>
                                    Historial
                                </a>
                            </div>
                        </div>`;
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

            $('#tblDet').DataTable({
                language: {
                    'url': 'https://raw.githubusercontent.com/Jhon-Paillacho/ERP-estaticos/main/language.json'
                },
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                order: [[0, "desc"]],
                //data: data.det,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "fecha"},
                    {"data": "impuesto"},
                    {"data": "interes"},
                    {"data": "multa"},
                    {"data": "servicios_administrativos"},
                    {"data": "total"},
                ],
                initComplete: function (settings, json) {

                }
            });
            $('#myModelDet').modal('show');
        })
})