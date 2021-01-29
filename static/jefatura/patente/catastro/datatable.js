function lista_catastro(){
    $('#tableCatastro').DataTable({
    language: {
        "decimal": "",
        "emptyTable": "No hay información",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
        "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
        "infoFiltered": "(Filtrado de _MAX_ total entradas)",
        "infoPostFix": "",
        "thousands": ",",
        "lengthMenu": "Mostrar _MENU_ entradas",
        "loadingRecords": "Cargando...",
        "processing": "Procesando...",
        "search": "Buscar:",
        "zeroRecords": "Sin resultados encontrados",
        "paginate": {
            "first": "Primero",
            "last": "Último",
            "next": "Siguiente",
            "previous": "Anterior",
        },
    },
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
        { "data": "ruc"},
        // { "data": "razon_social"},
        { "data": "tipocontribuyente"},
        { "data": "nombre_establecimiento"},
        { "data": "total_patrimonio"},
        { "data": "exonerada"},
        { "data": "acciones"},
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
                if (!row.suspendida && !row.exonerada){
                    return '<span class="badge badge-light">Normal</span>';
                }
                if (row.exonerada){
                    return '<span class="badge badge-success">Exonerada</span>';
                }
                if (row.suspendida){
                    return '<span class="badge badge-danger">Suspendida</span>';
                }

            }
        }
    ],
    initComplete: function(settings, json) {
        // alert('Datos cargados');
    }
    });
}

$(document).ready(function () {
    lista_catastro();
})