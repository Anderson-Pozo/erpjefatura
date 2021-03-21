$(() => {
    $('#tableVistaEstablecimiento').DataTable({
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
                'action': 'search_establ',
            }, // parametros
            dataSrc: ""
        },
        columns: [
            {"data": "nombre"},
            {"data": "fecha_inicio_actividad"},
            {"data": "total_patrimonio"},
            {"data": "tipo_actividad"},
            {"data": "direccion"},
            {"data": "estado"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: true,
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
});
