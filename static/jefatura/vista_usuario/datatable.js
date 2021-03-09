$(() => {
    let table = $('#tableVistaUsuario').DataTable({
        language: {
            'url': 'https://raw.githubusercontent.com/Jhon-Paillacho/ERP-estaticos/main/language.json'
        },
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
            {"data": "estado_pago"},
            {"data": "ruc"},
            {"data": "nombre_contribuyente"},
            {"data": "nombre_establecimiento"},
            {"data": "total_patrimonio"},
            {"data": "estado"},
            {"data": "acciones"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<a rel="historial" class="btn btn-datatable btn-icon btn-outline-secondary mr-2"' +
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
                    return row.estado;
                }
            }
        ],
        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });

    $('#tableVistaUsuario tbody')
        .on('click', 'a[rel="historial"]', function () {
            let tr = table.cell($(this).closest('td, li')).index();
            let data = table.row(tr.row).data();
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
            $('#modalHistorial').modal('show');
        })
});

// $(document).ready(() => lista_vista_usuario());
